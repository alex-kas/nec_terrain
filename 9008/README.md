### NEC Terrain 9008 guide

**GUYS, IT IS IF you have bricked your phone in a soft way, i.e. without dropping from the window of some 10th floor**

**This is COOL and courageous, but not difficult**

**This is under LINUX, windows sufferers should find their way**

**This is MEC Terrain specific**

#### 9008 explained

This is the mode in which the external usb port of your phone is enumerated as `05c6:9008` and is recognized a serial port, i.e. TTYn (COMn in windows). This happens if you so much messed up your phone that it cannot reach boot or recovery partitions. For example, erased aboot ... In this case your phone upon pressing power button shows you _NOTHING_. However, it is very likely still alive.

Now upon connection to your computer via usb you see _NOTHING_. You must activate the 9008 mode which is indeed you **LAST** chance. But this chance is quite steady and patient. In this mode you can reload the content of your internal flash by means of a simple script under linux. (In windows you must use special drivers and the QPST suite.) Note that your linux kernel must support serial TTY through usb.

Another situation when this mode can be useful is when you messed up your system not heavily but enough to say bye to your phone. For example, it boots but then enters some bootloop and unfortunately you did not install some normal (e.g. mine in case of NEC Terrain) recovery. Then you might need to reflash the whole system folder or just update recovery without being able to boot. Your savior is the 9008 mode.

All referred files are in this folder.

#### 9008 activation

* Remove the battery and the usb cable from the phone
* Glue off the sticker with you IMEI
* Observe a group of 4 contacts. The 2 in the middle are named GND and ENG_BOOT (from engineering), see `photo1.jpg` and `photo2.jpg`
* Connect you phone in this state (w/o a battery) to your computer
* Check with `lsusb` that it is _not_ seen, just in case
* Shorten for some short time GND and ENG_BOOT contacts, a tweezer from the Swiss army knife is enough.
* Check with `lsusb` that it is **seen** as `05c6:9008`; if not, repeat the previous step more carefully
* Notice that touching neighbour contacts seem to have no effect (including no harm)
* Also you **must not** keep contacts shortened and you **must not** insert battery.

My credits about shortening the contacts in question go to VANOLEO from xda. Thanks, dude!

You just have proven your phone is **ALIVE**. Keep on

#### Stage 1

Your phone is alive but it is NOT yet submissive. You must have a very special file. It is named programmer and is named like `MPRG8960.bin`. It can be in `HEX` format, i.e. `MPRG8960.HEX` but we have `hex2bin` converter. `M` in the name is some index letter, `8960` - the QualComm chip model. The crucial obstacle that this file is quite brand dependent. Literally, this took me more than a month to locate one, presumably from Casio 811, which eventually has done the job. I was lucky, I guess! This is why I renamed it as `MPRG8960NECTerrain.bin` to alert that it is a brand-specific thing.

The technique is as follows. In the 9008 mode your phone is still quite useless. It can accepts only special commands and data for use by the primary processor module. You have to switch the phone to another mode (not 9006, apparently as some sources claim) in which it can write data to its internal flash memory (notice, that for NEC Terrain it is not a 9006 mode, in which the internal flash would be seen as an SD card). To this aim you submit this special `MPRG8960NECTerrain.bin` file by means of the serial protocol and then send a command to execute this file as a program internally in the phone. Upon all of that you can use the serial protocol to write data to the internal flash.

The command is
```
sudo ./stage1.py -v MPRG8960NECTerrain.bin
```
It must be under root, `-v` is for the verbosity (you can omit). If no errors, you see `Done` as the last line. You need `python` and `pyserial` installed to have this working. Now you should wait. I could not determine how long, but at least few seconds before going to stage 2.

**DO NOT touch cable, keep connected, NO battery insertion, RELAX**

#### Stage 2

It is a bit more tricky. You are now ready to write to the internal flash. I took the initial scipt from Droid Ultra unbrick thread by VBlack on xda, so I preserved his strategy.

You must have a file which is the partition table of your phone as position of partitions is vital for the script in question. Which you cannot get as your phone dead. SO, you must assume one from a working identical phone around, from another person, from here for instance (`gpt.txt`), or from whatever. No help here, sorry.

What is the **MOST** important, you **MUST** understand what you want to rewrite. In my case I killed `aboot` experimenting with a new kernel and had to rewrite `aboot`. For a friend of mine I have rewritten `recovery` to save the system folder. As the rule of thumb:

**you can assume that if you are not me, you have altered your phone only by my instructions (or terroot written after my method) and therefore partitions are wither in their original state (of you did not touch your phone) or where they should be after my guides**

Therefore, the `gpt.txt` found in this folder is quite nice to locate most vital partitions (for this gpt `recovery` partition is as it is _after_ rooting by my guides). If ever needed, you will rewrite some of `sbl1,2,3`, `aboot`, `tz`, `rpm` or `recovery`, I think.

If you have your partition table in a form of binary file, you can make a text table by means of `gpt_parser.py`.

In `gpt.txt` the first column is the offset of partitions in bytes, names and their sizes

**!!!YOU DO NOT EVEN THINK TO TOUCH PARTITIONS `modemst1` and `modemst2` BY ANY MEANS!!!**

Once you understand what exactly you are going to change you edit the script `stage2.py`. You find the definition
```
BOOT_PARTITIONS = ("recovery",)
```
and change `recovery` to the partition name you want to rewrite. Name must appear **EXACTLY** as it is in the partition table file. If you want to rewrite only one partition, you **keep** the comma after, it is correct. If you want to rewrite more than one partition at once, you act like in the commented line in the script file just above. For example
```
BOOT_PARTITIONS = ("recovery","aboot")
```
with no trailing comma.

For each partition specified in the `BOOT_PARTITION` list you need a separate image file with extension `.img`, e.g. `recovery.img`, `aboot.img`, etc. Names are case sensitive and **MUST** coincide with the names of partitions.

There is a possibility to rewrite the partition table itself, but this seems to be indeed weird. I have not explored this to details.

Finally, given you have edited the `BOOT_PARTITION` variable, all `.img` files in place and a file a la 'gpt.txt' you are good to go. The command is
```
sudo ./stage2.py -v -ptf gpt.txt
```
Again, under root, `-v` for the verbosity and can be skipped, `-ptf` - option to specify the partition table file. Be careful, `-pt` is reserved to indicate that partition table itself must be rewritten. As said before, I did not explore this functionality to details.

If the script exits quickly mentioning errors, it means, you waited to few after the stage 1. It may also say that the phone is in stage 1 yet, so just go back. However, if there are indeed errors the serial modem will be reset. In this case you have to
* check with `lsusb` that the connection has gone (no `05c6:9008` device)
* shorten again GND and ENG_BOOT
* check that connection has reestablished
* if no connection, remove cable and go anew to stage 1

Normally writing goes quite slow (serial port). So, `-v` option is useful to see the progress. On success the last line in the output will be be `Done`.

If you understand that you want to rewrite one more partition, you go to stage 1 again as the modem has been reset.

#### DONE

Provided you did what you meant to, you get what you wanted.

I got 2 phones resurrected from dead.

**GOOD LUCK!**
