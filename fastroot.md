### Fast root guide for NEC Terrain

For those not common with adb/linux/etc:
* ALL commands are typed on your pc in terminal (`cmd` shell in windows)
* One line - one command
* You type (or copy) a command, press `enter`, wait the result and the new prompt
* after a command execution you see its output, it should be positive or neutral. If you see somewhat like "file not found", "command not found", "cannot ...", etc this most likely inidcates a mistake in your command, absence of vital files, or other oddity
* capital and literal letters are DIFFERENT
* NO unneeded symbols (well in some places I put a second command, for windows; hope it is understandable, what is exactly meant there)

#### Downloads

You preferably download everything to one directory on your pc

From folder `recovery/` in this repository:
* `adbtestgpt.sh (adbtestgpt.bat for windows)`
* `adbr.sh (adbr.bat for windows)`
* `flash_recovery.sh`
* `run_root_shell`
* `sgdisk`
* `kas.recovery.bin`

From folder `boot/` in this repository:

* `adbb.sh (adbb.bat for windows)`
* `build.prop`
* `kas.boot.bin`

From folder `system/` in this repository:

* `superuser.tar.gz`

#### Micro-sd card

You need a micro-sd card to be in the phone. It should have few gigabytes of space and be formatted as an mbr with a partition.

In linux this means that the card is seen as
```
/dev/mmcblk0
```
and its partition as
```
/dev/mmcblk0p1
```
In simpler words, if you examine your SD card in `disks` utility on your pc you should see:
```
Partitioning: Master Boot Record
Device: /dev/mmcblk0p1
Contents: vfat
```

In windows this means that when you see the inserted sd-card and analyse its properties the corresponding window in the tab `Volumes` says
```
Partition style MBR
```
and shows one volume.

The partition (volume) must be formatted as `vfat`

#### Pre-test

In linux check that `adbtestgpt.sh` has permissions 755. To be sure just issue on your pc inside the directory
where all the stuff has been saved
```
chmod 755 adbtestgpt.sh
```
Now boot your phone normally, into its canonical stock boot configuration. Connect the usb cable. In linux **NO** driver needed. For windows, driver (working in win7pro_x64) and `adb.exe` can be found in `system/` folder in this repository, file `adbfb.tar.gz`.
Also 'USB debugging' must be turned on in the phone.

Start `adb` daemon for exmaple by
```
sudo adb devices
(adb start-server [for windows])
```
and run the script (you should be inside the folder where you have just downloaded the stuff)
```
./adbtestgpt.sh
(adbtestgpt.bat [for windows])
```
You will see the partition table. The corenerstone is the gap between partitions 3 and 4
```
Number  Start (sector)    End (sector)  Size       Code  Name
   3          425984          557055   64.0 MiB    FFFF  fatallog
   4          589824          590335   256.0 KiB   FFFF  sbl1
```
it should be **ABSOLUTELY EXACTLY** as written above (on a non-altered phone).

**The script does not take decisions. It is you, who compares and decides what to do!**

If you are happy, continue!

#### New recovery

In linux check that `adbr.sh` script has permissions `755`. To be sure just issue on your pc inside the directory where all the stuff has been saved
```
chmod 755 adbr.sh
```
Run the script
```
./adbr.sh
(adbr.bat [for windows])
```
The very new recovery is ready to use!

#### New boot

In linux check that `adbb.sh` has `755` permissions. To be sure simply issue from inside the directory where you have downloaded the files
```
chmod 755 adbb.sh
```
**The microsd-card must be __in__ the phone.**

Run on your pc
```
./adbb.sh
(adbr.bat [for windows])
```
To copy files to a proper location on your sdcard (folder named `brnects0.715`).

Now restart your phone into *recovery* typing on your pc
```
adb reboot recovery
```
Wait at least the 'NEC' logo. After the 'NEC' logo this recovery shows **NOTHING**. Now go into shell (we will continue typing on the pc, of course, but virtually we will be in the phone)
```
adb shell
```
and do inside the shell
```
cd /rbin
./flash_boot.sh
```
Now exit the shell
```
exit
```
to come back to your pc and reboot the phone
```
adb reboot
```
The very new boot image is here!

#### Re-partitioning

Sorry, no short instruction yet.

#### Placing `su` and `Superuser.apk`

First unpack `superuser.tar.gz`

Boot the phone into the *recovery* mode by pressing *vol-down+power*. From the directory where you have downloaded the suepruser stuff do
```
adb push su /tmp
adb push Superuser.apk /tmp
adb shell
```
Now you are in the adb shell. Do there
```
cd /tmp
mount /dev/block/mmcblk0p12 /system
cp su /system/xbin/su
chown 0:0 /system/xbin/su
chmod 6755 /system/xbin/su
ln -s /system/xbin/su /system/bin/su
cp Superuser.apk /system/app
chmod 644 /system/app/Superuser.apk
umount /system
exit
```
Now you are back to your pc. Reboot the phone by
```
adb reboot
```
After the reboot you will see "Android is upgrading" meaning it installs a new 'system' program Superuser.apk

**DONE! Your phone is rooted!**
