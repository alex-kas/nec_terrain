## NEC Terrain

_As the name of the project suggests all the resources here are devoted to the NEC Terrain mobile phone. As such all
the resources here are specific to this phone (even though theoretically applicable to another one). Moreover, various subjective statements reflect my **personal** opinion._

### Specifications and goods

To be more precise we are talking about the following phone (the info from the `about` menu inside the phone):
* Model number: NE-201A1A
* Android version: 4.0.4
* Baseband version: N126400001
* Kernel version: 3.0.8 ncmc@ncmc #2 SMP PREEMPT Thu Sep 26 17:01:21 IST 2013
* Build number: 126460101

and the full specifications can be found [here](http://www.gsmarena.com/nec_terrain-5553.php).

In short, this is a heavily protected phone, all-proof (water, dust, salt, ...) with QWERTY physical keyboard which is also water-proof. You can type under the rain. It is reasonably fast: 1.5GHz dual-core CPU and it even has 1GB of RAM. The stock configuration has Android 4.0.4. Its internal memory is 8GB. Seems like a unique combination in the world of all phones.

In fact the king property is the physical keyboard. If someone wonders why: the physics of a touch screen is such that its functionality is almost absolutely screwed up in a presence of water-drops. Under the rain or a wet snow, or if your fingers are wet. You are just unable to operate a phone w/o a keyboard in such conditions.

Leaving the keyboard aside, this phone is comparable to Samsung Galaxy S4 Active or even outperformed by Casio Commando 4G LTE, Samsung Galaxy S5 Active and Samsung Galaxy S6 Active. However, my life-style demands the physical keys to be.

### Odds

This phone has several serious odds:

* It is discontinued. No updates are expected even though the phone itself is capable for KitKat at least
* Its partition scheme is as awful as that:
  * 800MiB for programs installed by you. Practically nothing, just updates to the system apps get it all immediately
  * 4.3GiB for your files, like photos, video, but *not* programs
* Tethering cannot be enabled
* A bug (one so far) was found which brings the phone to reboot if a program needs to read big set of data files

The less severe problem is the big amount of bloatware.

### Table of contents

1. [General theory](general-th.md) - is a worth reading text which explains what is rooting, nand-lock, bootloader unlocking, and why these are different and sometimes disconnected things. Also many terms are explained there.
2. [Exploit](exploit-th.md) - explains the theory of how the NEC Terrain is exploited
3. [Pre-requisits](exploit-pre.md) - lists mandatory pre-requisits to exploit the NEC Terrain
4. [New Recovery](../blob/master/recovery-howto.md) - desciption of the new recovery image and a step-by-step instruction to install one
5. [Re-partitioning](../blob/master/repartitioning-howto) -  a step-by-step instruction to re-partition the internal memory
6. [New Boot](../blob/master/boot-howto.md) - description of the new boot image,  a step-by-step instruction to install one
7. [System modification](../blob/master/system-howto.md) -  several useful howto-s on system modification
8. [Debloating](system/README.md) - lists of apps which can be disabled and why, and which *cannot* be disabled and why

### The concept

The just presented concept implements an idea of  a fully independent recovery. This means that if you mess up `/system` directory
you have chances to sort things out. You need this in particular if you want to repartition the internal memory - you just should __not__ do it on a live system or for the sake of security.
Originally you have almost no space for your programs (800MiB) and more than 4GiB just for photos, video, etc.

*Note that the original recovery lacks of ability to restore `/system`. Stock recovery presumes your `/system` could not be modified*

#### New recovery by hands

You can go a more linux-terminal way if you like instead of **terroot**.

* **recovery/** - folder: the proper recovery image is there

To install new recovery into its proper place, i.e. recovery partition, You download `adbr.sh`, `flash_recovery.sh`, `run_root_shell`, `sgdisk` and one of the `.bin` images from the `recovery/` folder here into one folder on your pc. Check that `run_root_shell`, `sgdisk` and both `.sh` scripts have permissions `755`.
**IMPORTANT:** whatever image you download you **must** save it under the name `kas.boot.bin` locally on your pc.

Now boot your phone normally, into its canonical stock boot configuration. Connect usb cable and execute on your pc (you should be inside the folder where you have just downloaded the stuff)
```
./adbr.sh
```
*If it complains, this means that perhaps you have not started `adb` before. Or maybe you have to use root to start it? On my pc I must initiate `adb` using*
```
sudo adb devices
```
*also check cables :)*

As the result you will have a brand new recovery image to be booted with *vol-down+power* pressed.


#### Repartitioning userdata and GROW

Re-partitioning  is a straightforward but a *must-to-be-done-accurately* procedure. Mistakes may cost you a phone.

---

Before turning on your phone: you must have an sd-card IN it.

If you plan a backup (see below), prepare a BIG miscro-sd card which will hold all your data from userdata and GROW partitions. Originally they total to 5GiB but actual files may use less.

*Your microsd card MUST be formatted such that it has an `mbr` and a partition. It is usually like that nowadays but if not, change it to have an `mbr`.
In other words this card in a pc linux should be seen as `/dev/mmcblk0` and its partition as `/dev/mmcblk0p1`. If you do not see the later, create `mbr` and a partition anew on your pc.*

---

Boot into the new recovery with *vol-down+power* pressed. On the phone you will see tiny (sorry) green text proving that things have really changed. Do on your pc
``
adb shell
``
and you see the root shell prompt
```
/#
```
Availability of adb is the most serious achievement of this new recovery.

Remember: It is immediately root.

**BE CAREFUL!!! IT IS THE PROPER ROOT!!! NO LIMITS!!!**

Use adb, do not go into the stock recovery program even though it is still accessible with *vol-up* and then *vol-down*. It is useless. It is just do display my new greeting :)

You have in your disposal `busybox` (with all links), `gdisk`, `sgdik`, `mkfs.ext4` and `mksh` in `/sbin` folder. It is a good linux recovery set of tools. Also you have
some essential scripts in `/rbin`.
`/rbin` is NOT in your path so you will not run scripts from there unintentionally.

**You are ready for adventure!**

##### Step 1. Backup.

Skip it if you do not care neither about your files nor about settings or programs installed by you and (therefore) want an effect of *factory reset*

If you care about something of the above - do backup. It is as follows (commands inside the adb shell)
```
cd /rbin
./bu_data.sh
```
You will see a long output listing each file added to an archive on your sdcard in a very special folder `brnect08.715`

##### Step 2. Actual re-partitioning

For this just run
```
gdisk
```

Unfortunately, I cannot provide you help here as it is solely up to you HOW you want to breakdown partitions. Just for reference, originally the partitions of interest reside as
```
   13         2818048         4456447   800.0 MiB   8300  userdata
   14         4456448        13565951   4.3 GiB     FFFF  GROW
```
where start and end are in 512-byte-sectors. I did them like
```
   13         2818048        13303807   5.0 GiB     8300  userdata
   14        13303808        13565951   128.0 MiB   FFFF  GROW
```
You achieve this in `gdisk` by deleting a partition and recreating it again with new boundaries.

Tiny `gdisk` intro:

All modifications are in MEMORY! It is safe, but DO NOT FORGET TO WRITE, using command **w** before you quit.

* **?** - anytime for help
* **d** - delete partition, it asks number: enter number and press `enter`
* **n** - create new partition, it asks number. If say, you deleted partition number 14, you now can enter 14, so you will just redo it, but of another size. Then starting and ending sectors are asked. You can just get from the table above. OR invent YOURS! As you like. Then it asks about a flag, agree to 8300, even for GROW. Standartly FFFF flag is not supported
* **c** - CRUCIAL: you **MUST** give it a name as it was before, **EXACTLY**. Before entering the name you will be asked the partition number, of course
* **p** - print, how the table looks now
* **w** - write changes to disk, w/o this you will loose your efforts!
* **q** -- quit

Once created AND WRITTEN by issuing the command `w` INSIDE `gdisk` you MUST reboot. It is the only way to instruct the kernel to read new partition table. Do it from your pc via
```
adb reboot recovery 
```
After the reboot you are back to the recovery environment.

##### Step 3. Formatting

Go into the shell by typing on your pc
```
adb shell 
```
Now you MUST create file-systems on your re-shuffled partitions (command inside the adb shell)
```
mkfs.vfat /dev/block/mmcblk0p14
mkfs.ext4 -b 1024 -i 4096 /dev/block/mmcblk0p13
```
You are kindly instructed to write the arguments for the ext4 formatiing exactly as they are here. These values of `-b` and `-i` will save you from vasting 25% of the `userdata` space for NOTHING!

After this you will have a system *EXACTLY* like after a stock factory reset. Note, stock factory reset just simply erases ALL on userdata and GROW partitions. Nothing more.

*Remember, even the stock factory reset does not change `/system` back. There is no "back" for `/system` in this phone. This means you cannot get a REALLY stock configuration, 
unless you ask someone to provide you one.*

*So, saying "factory reset" I mean your files, settings and programs installed by you wiped.*

###### Step 4. Restoring your files

Skip it if already skipped the step 1 or if you have changed your mind and want a factory reset phone.

To restore your files issue inside the adb shell
```
cd /rbin
./rr_data.sh
```
This will unpack all your files from the backup into the previous place like nothing have happened!
The recovery program is still active: you can press *vol-up* and then *vol-down* to activate it, then choose the reboot option there. Or simply exit the shell
```
exit
```
and then type on your pc
```
adb reboot
```
After the reboot you either have your previous phone or will have to re-do all the initialization. This depends on whether you have backed-up files and restored them back or not.

So to say: **DONE!**

#### Placing boot image by hands

It is done by **terroot** but, if you like: how you place the boot image without **terroot**. The image is in

* **boot/** - folder

To install new boot into its proper place, i.e. boot partition, you download `adbb.sh`, `build.prop` and one of the the `.bin` images from the `boot/` folder here to some place on your pc. Check that `adbb.sh` has `755` permissions.
**IMPORTANT:** whatever image you download you **must** save it under the name `kas.boot.bin` locally on your pc.

Your phone must be booted normally.
Run on your pc (you are inside the directory where you downloaded the files)
```
./adbb.sh
```
To copy files to a proper location on your sdcard (folder named `brnects0.715`), which must be in the phone.

#### Flashing another boot image

Restart your phone into recovery typing on your pc
```
adb reboot recovery
```
Now go into shell
```
adb shell
```
and do inside the shell
```
cd /rbin
./flash_boot.sh
```
It will copy the current boot image to sdcard under the name `brnects0.715/boot.current.bin` and flash `kas.boot.bin` into place. On top of this we have to update `build.prop` file.
I suggest doing all by hands, even though I can write a script. But it may happen you want to see how to do this in order to do another tinkering next time w/o a help
```
mount /dev/block/mmcblk0p12 /system
mount /dev/block/mmcblk1p1 /sdcard
cd /system
cp /sdcard/brnects0.715/build.prop .
chmod 644 build.prop
cd /
umount /system
umount /sdcard
```
Comments: you first mount the actyal system to the folder `/system`; then sdcard to the folder `/sdcard`; then you go inside of the system via `cd` and copy the `build.prop` file from sd card there (mind the final dot `.` in the `cp` command, it means the folder where you are *now*); then you change permission for `build.prop`; quit to the root folder `/`; and finally unmount mounted partitions using `umount`. The later step ensures all data which could be in cache are really written

This is *the* way you should do **whatever** with your system next time.

A believe it is much safer and less stressful then on a live system.

Now
```
exit
```
to come back to your pc and
```
adb reboot
```
**DONE!**

A believe all of that is much safer and less stressful then on a live system.

#### Troubleshooting

Interaction of your pc with the phone may stall. No clue why exactly but if you believe that some operation cannot last so long you can try to wake up `adb` either by
trying `adb shell` from another terminal on your pc or by unplugging/re-plugging the usb cable. In extreme case you may have to take the battery off, then place it back and then boot your phone
with *vol-down* pressed. (the latter happened to me only once).

Notice that some operations take indeed long time. Sometimes mounting of a partition takes up to 15 seconds. Again, no clue, why.
