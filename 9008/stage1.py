#!/usr/bin/python
V = "1.2"
#History:
#V1.2 06/08/2014 - Add lot of information printing
#V1.1 29/07/2014 - Add windows tty port detection
#V1.0 28/07/2014 - Initial release
#(c) VBlack

import os, sys, array, time, glob, argparse, platform, struct

VERSION = 0
FLASH = 0

#PBL stage packet
PACKET_ACK = array.array('B',[0x02])
PACKET_EXECUTE = array.array('B',[0x05])
PACKET_NO_OP = array.array('B',[0x06])
PACKET_REQUEST_PARAM = array.array('B',[0x07])
PACKET_RESET_PBL = array.array('B',[0x0a])
PACKET_VERSION = array.array('B',[0x0c])
PACKET_WRITE_CHUNK_PBL = array.array('B',[0x0f])
PACKET_SERIAL_7 = array.array('B',[0x014])
PACKET_SERIAL_8 = array.array('B',[0x016])
PACKET_HW_ID = array.array('B',[0x17])
PACKET_PUBLIC_KEY = array.array('B',[0x18])
PACKET_REQUEST_DLOAD = array.array('B',[0x3a])

#SBL stage packets
PACKET_MAGIC = array.array('B',[0x01,]) + array.array('B',"QCOM fast download protocol host") + array.array('B',[0x07, 0x05, 0x09])
PACKET_WRITE_CHUNK_SBL = array.array('B',[0x07])
PACKET_RESET_SBL = array.array('B',[0x0b])
PACKET_CLOSE_FLUSH = array.array('B',[0x15])
PACKET_SECURE_MODE = array.array('B',[0x17, 0x01])
PACKET_OPEN_MULTI = array.array('B',[0x1b, 0x21])
PACKET_QFUSE_READ = array.array('B',[0x34])

PFILE_ADDRESS = 0x2a000000

CHUNK_SIZE = 1024

#BOOT_PARTITIONS = ("sbl1", "sbl2", "sbl3", "aboot", "rpm", "tz")
BOOT_PARTITIONS = ("aboot",)

PT_PARTITION = "partitions"

VERBOSE = False

crcTable = (
    0x0000, 0x1189, 0x2312, 0x329b, 0x4624, 0x57ad, 0x6536, 0x74bf,
    0x8c48, 0x9dc1, 0xaf5a, 0xbed3, 0xca6c, 0xdbe5, 0xe97e, 0xf8f7,
    0x1081, 0x0108, 0x3393, 0x221a, 0x56a5, 0x472c, 0x75b7, 0x643e,
    0x9cc9, 0x8d40, 0xbfdb, 0xae52, 0xdaed, 0xcb64, 0xf9ff, 0xe876,
    0x2102, 0x308b, 0x0210, 0x1399, 0x6726, 0x76af, 0x4434, 0x55bd,
    0xad4a, 0xbcc3, 0x8e58, 0x9fd1, 0xeb6e, 0xfae7, 0xc87c, 0xd9f5,
    0x3183, 0x200a, 0x1291, 0x0318, 0x77a7, 0x662e, 0x54b5, 0x453c,
    0xbdcb, 0xac42, 0x9ed9, 0x8f50, 0xfbef, 0xea66, 0xd8fd, 0xc974,
    0x4204, 0x538d, 0x6116, 0x709f, 0x0420, 0x15a9, 0x2732, 0x36bb,
    0xce4c, 0xdfc5, 0xed5e, 0xfcd7, 0x8868, 0x99e1, 0xab7a, 0xbaf3,
    0x5285, 0x430c, 0x7197, 0x601e, 0x14a1, 0x0528, 0x37b3, 0x263a,
    0xdecd, 0xcf44, 0xfddf, 0xec56, 0x98e9, 0x8960, 0xbbfb, 0xaa72,
    0x6306, 0x728f, 0x4014, 0x519d, 0x2522, 0x34ab, 0x0630, 0x17b9,
    0xef4e, 0xfec7, 0xcc5c, 0xddd5, 0xa96a, 0xb8e3, 0x8a78, 0x9bf1,
    0x7387, 0x620e, 0x5095, 0x411c, 0x35a3, 0x242a, 0x16b1, 0x0738,
    0xffcf, 0xee46, 0xdcdd, 0xcd54, 0xb9eb, 0xa862, 0x9af9, 0x8b70,
    0x8408, 0x9581, 0xa71a, 0xb693, 0xc22c, 0xd3a5, 0xe13e, 0xf0b7,
    0x0840, 0x19c9, 0x2b52, 0x3adb, 0x4e64, 0x5fed, 0x6d76, 0x7cff,
    0x9489, 0x8500, 0xb79b, 0xa612, 0xd2ad, 0xc324, 0xf1bf, 0xe036,
    0x18c1, 0x0948, 0x3bd3, 0x2a5a, 0x5ee5, 0x4f6c, 0x7df7, 0x6c7e,
    0xa50a, 0xb483, 0x8618, 0x9791, 0xe32e, 0xf2a7, 0xc03c, 0xd1b5,
    0x2942, 0x38cb, 0x0a50, 0x1bd9, 0x6f66, 0x7eef, 0x4c74, 0x5dfd,
    0xb58b, 0xa402, 0x9699, 0x8710, 0xf3af, 0xe226, 0xd0bd, 0xc134,
    0x39c3, 0x284a, 0x1ad1, 0x0b58, 0x7fe7, 0x6e6e, 0x5cf5, 0x4d7c,
    0xc60c, 0xd785, 0xe51e, 0xf497, 0x8028, 0x91a1, 0xa33a, 0xb2b3,
    0x4a44, 0x5bcd, 0x6956, 0x78df, 0x0c60, 0x1de9, 0x2f72, 0x3efb,
    0xd68d, 0xc704, 0xf59f, 0xe416, 0x90a9, 0x8120, 0xb3bb, 0xa232,
    0x5ac5, 0x4b4c, 0x79d7, 0x685e, 0x1ce1, 0x0d68, 0x3ff3, 0x2e7a,
    0xe70e, 0xf687, 0xc41c, 0xd595, 0xa12a, 0xb0a3, 0x8238, 0x93b1,
    0x6b46, 0x7acf, 0x4854, 0x59dd, 0x2d62, 0x3ceb, 0x0e70, 0x1ff9,
    0xf78f, 0xe606, 0xd49d, 0xc514, 0xb1ab, 0xa022, 0x92b9, 0x8330,
    0x7bc7, 0x6a4e, 0x58d5, 0x495c, 0x3de3, 0x2c6a, 0x1ef1, 0x0f78)

flash_sizes = ["Invalid or unrecognized Flash device, or Flash device programming not supported by this implementation",
         "4-megabit (512 K byte) Flash",
         "8-megabit (1024 K byte) Flash",
         "16-megabit (2048 K byte) Flash used as an 8-megabit Flash",
         "16-megabit (2048 K byte) Flash",
         "32-megabit (4096 K byte) Flash",
         "64-megabit (8192 K byte) Flash",
         "Reserved"]

dev_types = ["Intel 28F400BX-TL or Intel 28F400BV-TL",
             "AMD Am29F400",
             "Intel 28F800BV-T",
             "AMD Am29LV400T",
             "AMD Am29LV800T",
             "Sharp LH28F400SUHT-LC15",
             "Hitachi HN29WT800T",
             "Texas Instruments TMS28F800SZT",
             "AMD Am29DL800T",
             "Intel 28F800B3-T",
             "Intel 28F160B3-T",
             "Sharp LH28F800BG-LT",
             "Mitsubishi 29GT161",
             "AMD Am29DL162",
             "Fujitsu 29DL162",
             "Atmel 49BV8192",
             "Fujitsu 29DL323",
             "Fujitsu 84VD22283",
             "AMD Am29DL163",
             "AMD Am29DL323",
             "Mitsubishi 29GT320",
             "Toshiba 50VSF2581",
             "NEC 222243A",
             "AMD Am29PDS322D",
             "Mitsubishi M6MGT641",
             "AMD Am29BDS640G",
             "Unknown or unrecognized device"]

nack_res = ["Illegal reason (do not use)",
            "Invalid frame FCS",
            "Invalid destination address",
            "Invalid length",
            "Unexpected end of packet",
            "Data length too large for buffer",
            "Unknown/invalid command",
            "Operation failed",
            "Wrong Flash intelligent ID",
            "Bad programming voltage",
            "Write-verify failed",
            "Not permitted without unlock",
            "Incorrect security code",
            "Cannot power down phone",
            "Operation not permitted at this time",
            "Invalid read address",
            "Illegal reason (do not use)"]

def openTTY(tty_path = ""):
    if tty_path == "":
        if platform.system() != 'Windows':
            product = ""
            vendor = ""
            dev = ""
            devices = map(lambda x: x.split("/")[-1],glob.glob("/sys/bus/usb/devices/*"))
            for device in devices:
                try:
                    with open("/sys/bus/usb/devices/%s/idProduct"%device, 'r') as f:
                        product = f.read()
                    with open("/sys/bus/usb/devices/%s/idVendor"%device, 'r') as f:
                        vendor = f.read()
                except:
                    pass
                if (vendor.strip() == "05c6") and (product.strip() == "9008"):
                    dev = device
                    break
            drivers = map(lambda x: x.split("/")[-1],glob.glob("/sys/bus/usb/devices/%s/%s:*"%(dev,dev)))
            for driver in drivers:
                ttys = map(lambda x: x.split("/")[-1],glob.glob("/sys/bus/usb/devices/%s/%s/tty*"%(dev,driver)))
                if len(ttys) >0:
                    tty_path = "/dev/%s"%ttys[0]
                break
        else:
            dload_port_desc = "Qualcomm HS-USB QDLoader 9008"

            port_list = list(serial.tools.list_ports.comports())
            ''' Loop through the available ports to find the COM port
            used for dload enumeration.
            Exit if multiple dload enumerations are found '''
            for port in port_list:
                if dload_port_desc in port[1]:
                    tty_path = port[0].lower()
                    break

    if tty_path != "":
        print "Found TTY port: ",tty_path
        tty = serial.Serial(port=tty_path, baudrate=115200)
        return tty
    else:
        print "Could not find Qualcomm device in Emergency download mode"
        return None

def closeTTY(tty):
    tty.close()

def serial16(data):
    out = array.array('B')
    out.append((data >> 8) & 0xFF)
    out.append(data & 0xFF)
    return out

def serial16le(data):
    out = array.array('B')
    out.append(data & 0xFF)
    out.append((data >> 8) & 0xFF)
    return out

def serial32(data):
    out = array.array('B')
    out += serial16((data >> 16) & 0xFFFF)
    out += serial16(data & 0xFFFF)
    return out

def serial32le(data):
    out = array.array('B')
    out += serial16le(data & 0xFFFF)
    out += serial16le((data >> 16) & 0xFFFF)
    return out

def crc(initial, packet):
    for byte in packet:
        initial = ((initial >> 8) & 0xFFFF) ^ crcTable[(initial ^ byte) & 0xFF]
    return ~initial & 0xFFFF

def escape(packet):
    out = array.array('B')
    for byte in packet:
        if byte == 0x7e:
            out.append(0x7d)
            out.append(0x5e)
        elif byte == 0x7d:
            out.append(0x7d)
            out.append(0x5d)
        else:
            out.append(byte)
    return out

def unescape(packet):
    escape = False
    out = array.array('B')
    for byte in packet:
        if escape:
            if byte == 0x5e:
                out.append(0x7e)
            elif byte == 0x5d:
                out.append(0x7d)
            else:
                print "Fatal error unescaping buffer!"
                return None
            escape = False
        else:
            if byte == 0x7d:
                escape = True
            else:
                out.append(byte)
    if len(out) == 0:
        return None
    return out

def sendPacket(tty, packet):
    c = crc( 0xffff, packet )
    out = array.array('B',[0x7e]) + escape(packet + serial16le(c)) + array.array('B',[0x7e])
    if VERBOSE:
        print "SENDING: ", " ".join("%02x" % b for b in out)
    tty.write(out)
    return True

def readPacket(tty, timeout, expect_packet = -1, expect_no_response = False):
    while True:
        buf = array.array('B')
        end = start = time.clock()
        
        while (end-start) <= timeout:
            if tty.inWaiting() > 0:
                curr = ord(tty.read(1))
                if len(buf) == 0:
                    if curr != 0x7e:
                        return None
                buf.append(curr)
                if (curr == 0x7e) and (len(buf) > 1):
                    break;
            end = time.clock()
        if len(buf) > 0:
            buf = buf [1:-1]
        buf = unescape(buf)
        
        if buf != None:
            if (buf[0] == 0x0e) and (expect_packet != buf[0]):
                if not expect_no_response:
                    print "\tLOG: ", buf[1:-2].tostring().strip()
                continue
                #return None
            elif (buf[0] == 0x0d) and (expect_packet != buf[0]):
                if not expect_no_response:
                    print "\tERROR: 0x%08x:"%struct.unpack("<I",buf[1:5]), buf[5:-2].tostring()
                return None
        else:
            if not expect_no_response:
                print "Failed to read response."
            return None
        
        if (expect_packet > 0):
            if (len(buf) < 1) or (buf[0] != expect_packet):
                if buf[0] != 3:
                    print "Invalid Response!!!: ", buf, expect_packet
                    return False
                nack = struct.unpack(">H",buf[1:3])[0]
                if nack > len(nack_res)-1:
                    nack = len(nack_res)-1
                print "ERROR: ", nack_res[nack]
                return None
        
        if VERBOSE:
            print "RECEIVED: ", " ".join("%02x" % b for b in buf)
        break
    return buf[:-2]

########################### PBL STAGE ##################################
########################### PBL STAGE ##################################
########################### PBL STAGE ##################################
########################### PBL STAGE ##################################
########################### PBL STAGE ##################################
########################### PBL STAGE ##################################
########################### PBL STAGE ##################################

def writeChunk_PBL(tty, address, chunk):
    if not sendPacket( tty, PACKET_WRITE_CHUNK_PBL + serial32(address) + serial16(len(chunk)) + chunk):
        print "Failed to send chunk"
        return False

    response = readPacket(tty, 2.0, PACKET_ACK[0])
    if None == response:
        return False

    return True

def uploadFile_PBL(tty, address, filename):
    data = array.array('B')
    print "Uploading file '%s' to addr 0x%x..."%(filename, address)
    try:
        with open(filename, "rb") as f:
            while True:
                try: data.fromfile(f, 2000)
                except EOFError: break
    except:
        print "File not found %s"%filename
        return False
    while len(data) > 0:
        chunk = data[:CHUNK_SIZE]
        data = data[CHUNK_SIZE:]

        if VERBOSE:
            print "Writing %d bytes to 0x%x; %d bytes left."%(len(chunk), address, len(data))
        if not writeChunk_PBL(tty, address, chunk):
            print "Upload failed"
            return False
        address += len(chunk)
    return True

def isStagePBL(tty):
    return doNoOp(tty)

def doGo(tty, address):
    print "Executing..."
    if not sendPacket( tty, PACKET_EXECUTE + serial32(address)):
        print "Failed execute"
        return False

    response = readPacket(tty, 5.0, PACKET_ACK[0])
    if None == response:
        return False

    time.sleep(2)
    return True

def doNoOp(tty):
    if not sendPacket( tty, PACKET_NO_OP):
        print "Failed No OP"
        return False

    response = readPacket(tty, 2.0, PACKET_ACK[0], expect_no_response = True)
    if None == response:
        return False
    return True

def doSoftwareVersion(tty):
    print "Requesting SoftwareVersion..."
    if not sendPacket( tty, PACKET_VERSION):
        print "Failed SoftwareVersion"
        return False

    response = readPacket(tty, 2.0, PACKET_VERSION[0]+1)
    if None == response:
        return False

    print "Version: ", response[2:2+response[1]].tostring()
    return True

def doSerialNum(tty):
    if VERSION < 7:
        return True
    print "Requesting SerialNumber..."
    if VERSION == 7:
        PACKET = PACKET_SERIAL_7
    else:
        PACKET = PACKET_SERIAL_8
    if not sendPacket( tty, PACKET):
        print "Failed SerialNumber"
        return False

    response = readPacket(tty, 2.0, PACKET[0])
    if None == response:
        return False
    sn_len = response[1]/8
    print "Serial number: ", ",".join("%02x" % b for b in response[2:2+sn_len])
    return True

def doHWId(tty):
    if VERSION < 8:
        return True
    print "Requesting HW Id..."
    if not sendPacket( tty, PACKET_HW_ID):
        print "Failed HW Id"
        return False

    response = readPacket(tty, 2.0, PACKET_HW_ID[0])
    if None == response:
        return False
    hwid_len = struct.unpack('>H', response[1:3])[0]/8
    print "HW Id: ", ",".join("%02x" % b for b in response[3:3+hwid_len])
    return True

def doPublicKey(tty):
    if VERSION < 8:
        return True
    print "Requesting PublicKey..."
    if not sendPacket( tty, PACKET_PUBLIC_KEY):
        print "Failed PublicKey"
        return False

    response = readPacket(tty, 2.0, PACKET_PUBLIC_KEY[0])
    if None == response:
        return False
    pkey_len = struct.unpack('>H', response[1:3])[0]/8
    print "PublicKey: ", ",".join("%02x" % b for b in response[3:3+pkey_len])
    return True


def doRequestDload(tty):
    print "Requesting Dload..."
    if not sendPacket( tty, PACKET_REQUEST_DLOAD):
        print "Failed requestDload"
        return False

    print "requestDload send ok"

    response = readPacket(tty, 2.0, PACKET_REQUEST_DLOAD[0])
    if None == response:
        return False

    return True

def doRequestParam(tty):
    print "Requesting Params..."
    if not sendPacket( tty, PACKET_REQUEST_PARAM):
        print "Failed requestParam"
        return False

    response = readPacket(tty, 2.0, PACKET_REQUEST_PARAM[0]+1)
    if None == response:
        return False
    if len(response) != 8:
        return False

    print "Params:"
    global VERSION
    VERSION = response[1]
    print "\tVersion: %d"%VERSION
    print "\tMin version: %d"%response[2]
    ws = struct.unpack('>H', response[3:5])[0]
    print "\tMax write size: %d (0x%08x)"%(ws, ws)
    print "\tModel: %d"%response[5]
    fs = response[6]
    if fs > len(flash_sizes)-1:
        fs = len(flash_sizes)-1
    global FLASH
    FLASH = fs
    print "\tDevice size: %s"%flash_sizes[fs]
    dt = response[7]
    if dt > len(dev_types)-1:
        dt = len(dev_types)-1
    print "\tDevice type: %s"%dev_types[dt]
    return True

def doReset_PBL(tty):
    print "Sending PBL Reset..."
    if not sendPacket( tty, PACKET_RESET_PBL):
        print "Failed Reset\n";
        return False

    response = readPacket(tty, 2.0, PACKET_ACK[0])
    if None == response:
        return False

    return True

def doStage_PBL(tty,pFile):
    response = readPacket( tty, 0.1, expect_no_response = True )
    while response != None:
        if VERBOSE:
            print "Ignoring response: ", response
        response = readPacket( tty, 0.1, expect_no_response = True )

    if doRequestParam(tty):
        if doSoftwareVersion(tty):
            if doSerialNum(tty):
                if doHWId(tty):
                    if doPublicKey(tty):
                        if FLASH != 0:
                            return doRequestDload(tty)
                        else:
                            if uploadFile_PBL(tty, PFILE_ADDRESS, pFile):
                                return doGo( tty, PFILE_ADDRESS )
    return False

#########################
#########################
#########################
#########################
#########################
#########################
#########################

def ParsePTfile(filename, pt_flash):
    try:
        f = open(filename)
    except:
        print "File not found %s"%filename
        return None

    path = os.path.dirname(os.path.abspath(filename))
    data = map(lambda x: map(lambda y: y.strip(),x.split(":")), f.readlines()[1:])
    file_s = set(map(lambda x: x[1], data))
    data = dict([d[1], [int(d[0],16),int(d[2])]] for d in data)
    if pt_flash:
        need_s = set(BOOT_PARTITIONS + (PT_PARTITION,))
    else:
        need_s = set(BOOT_PARTITIONS)
    if not need_s.issubset(file_s):
        print "Not all partitions present: ", need_s - (need_s & file_s)
        return None

    images = []
    for p in need_s:
        try:
            fn = path + '/' + p +'.img'
            if os.path.getsize(fn) > data[p][1]:
                print "File size %s bigger than partition"%fn
                return None
        except:
            print "Could not open file %s"%fn
            return None
        images.append([data[p][0], fn])
    images.sort()
    f.close()
    return images

def main():
    parser = argparse.ArgumentParser(description='Qualcomm DLOAD mode images upload utility.')
    parser.add_argument('-tty','--ttyPort', type=str, help='Optional ttyPort', default="")
    parser.add_argument('MPRGfile', type=str, help='MPRG file in .bin format')
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    tty = None

    print "QDLoad stage 1 utility version %s (c) VBlack 2014, ported by alex-kas"%V

    global VERBOSE

    if args.verbose:
        VERBOSE = True
            
    tty = openTTY(args.ttyPort)
    if tty != None:
        if VERBOSE:
            print tty.getPort()
        if isStagePBL(tty):
            if doStage_PBL(tty, args.MPRGfile):
                print "Done"
                return True
            else:
                doReset_PBL(tty)
        else:
            print "The device seems ready for stage 2"
            return True

    print "Done, with errors!!!"

    if tty != None:
        closeTTY(tty)
    return False

if __name__ == "__main__":
    #Verify python version is > 2.6 and < 3.0
    python_version = sys.version_info
    if python_version[0] != 2 or python_version[1] < 6:
        print("Python version 2.6 or 2.7 required!")
        print("you can download Python 2.6.x or 2.7.x here:")
        print("http://www.python.org/download/releases/")
        exit()

    # check whether pyserial 2.6 is installed.
    try:
        import serial
        import serial.tools.list_ports
    except ImportError:
        print("Please install pyserial 2.6 from here")
        print("https://pypi.python.org/pypi/pyserial")
        exit()

    main()
