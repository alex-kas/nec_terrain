### Fast root guide for NEC Terrain

#### Downloads

You preferably download everything to one directory on your pc

From folder `recovery` in this repository:
* `adbtestgpt.sh (adbtestgpt.bat for windows)`
* `adbr.sh (adbr.bat for windows)`
* `flash_recovery.sh`
* `run_root_shell`
* `sgdisk`
* `kas.boot.bin`

From folder `boot/` in this repository

* `adbb.sh (adbb.bat for windows)`
* `build.prop`
* `kas.boot.bin`

#### Pre-test

In linux check that `adbtestgpt.sh` has permissions 755. To be sure just issue on your pc inside the directory
where all the stuff has been saved
```
chmod 755 adbtestgpt.sh
```
Now boot your phone normally, into its canonical stock boot configuration. Connect usb cable.
Start `adb` daemon for exmaple by
```
sudo adb devices
(adb start-server [for windows])
```
and run the script
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
EXACTLY as written above (on a non-altered phone).

**The script does not take decisions. It is you, who compares and decides what to do!**

If you are happy, continue!

#### New recovery

In linux check that `adbr.sh` script has permissions `755`. To be sure just issue on your pc inside the directory where all the stuff has been saved
```
chmod 755 adbr.sh
```
Run the script (you should be inside the folder where you have just downloaded the stuff)
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

Run on your pc (you should be inside the directory where you downloaded the files)
```
./adbb.sh
(adbr.bat [for windows])
```
To copy files to a proper location on your sdcard (folder named `brnects0.715`).

Now restart your phone into recovery typing on your pc
```
adb reboot recovery
```
Wait at least the 'NEC' logo. After the 'NEC' logo this recovery shows **NOTHING**. Now go into shell
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



