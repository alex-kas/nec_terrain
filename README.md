# nec_terrain
Exploiting NEC Terrain mobile

.

.

.

Introduction and terroot

The pre-story can be found in http://forum.xda-developers.com/showthread.php?t=2515602
and many useful scripts, links and the most important the rooting app can be found in https://github.com/x29a/nec_terrain_root.
It is an easily traceable app which implements the method (my, in fact) outlined in
http://forum.xda-developers.com/showpost.php?p=61542922&postcount=186 (also a bit before and all way down)

A bit of info:

Terminology:

boot - normal boot via the image on the boot partition (number 9). The kernel in this image blocks rw access to the vital system areas, like system, boot, recovery, sbl1,2,3, aboot, rpm, tz.
You cannot write there even if you are root.

recovery - recovery boot (via vol-down+power) via the recovery partition (number 11). The kernel there is free of the write-blocks.

In order to root the phone we need to place the su binary inside /system/bin (or /system/xbin) and the goal is to open it for write. Since even root cannot do it, the new goal is to modify the boot
image where all mountings happen. But reflashing an image is not possible.

So, the goal is to flash it to a new place and instruct the system about this. Out of the sudden the gpt table itself is NOT protected from writing.
Moreover, the boot locker just a joke. It exists, it check certificates, hash, etc, but its ligic is like that:

1. If I see a wrong image I boot it anyway.

2. BUT I'll write one byte just inside my aboot image

3. Next time, if I see this byte set, I boot whatever you like w/o verification

4. ...

Good for us, less work.

In short the program, named terroot, does the following. Using the run_root_shell, which in turn uses a loop-hole in the kernel to achieve a temporary root,
terroot remaps the recovery partition into another location. This location is writable under a temporary root and you can flash there any image.
terroot in its present version flashes there an image composed of the following (recall that any boot image has 2 parts: kernel and init ramdisk to kick-off the system):

1) recovery kernel, because it has no protection over system partitions

2) boot ramdisk tinkered such that you get /system and / in rw modes and also a property att.service.entitlement is set to false so that you can tether.

So at this stage you can do the following: boot as normal and have your normal system or boot as recovery and have a feeling of a normal system but w/o limits and with /system already rw.
You still however, need to use run_root_shell to have a root environment. But now, using it you can place, say su binary into /system/bin

To proceed with further steps you MUST run terroot at least once. It is essential to remap the recovery partition in another location. Alternatively you can do it by hands following the xda thread.

What is next you may ask? What apart from root?

One of the greatest problems of this phone is its partitioning. It has 800MB for userdata (where you install your programs) and 4.3GB for GROW (for your photos in fact).

.

.

.


Repartitioning userdata and GROW

It is a straightforward but subtle thing. Mistakes may cost you a phone. My ideology is that you MUST create an isolated environment for this. Otherwise your phone may become a brick. Remember, it is a pc,
you cannot boot from a flash and revert things.

The current idea is to use recovery as the proper recovery and boot as the normal boot. So I assume that coming to this quest you have you Terrain with you which has undergo the terroot
treatment at least once. Otherwise, go up, read, and do. Then return here.


Current files:

boot/ - good boot image, better, I think then currently terroot uses (I'm straight in phrasing here as the prebious image was also cooked by me, I think I have right to compare)

recovery/ - the proper recovery image

First, we install new recovery (into its proper, i.e. recovery partition) You download all (3) files from the recovery folder into one folder on your pc. Check that run_root_shell 
and adbr.sh have proper permissions 755.

Now boot your phone normally, into its canonical stock boot configuration. Connect usb cable and execute

./adbr.sh

on your pc. As the result you will have a brand new recovery image to be booted with vol-down pressed.

Well, you have lost an achievement of terroot and do not have a possibility to boot such that /system is rw. But wait, we are working now exactly for that but I guess in a safer way. So, let's go further.

.

You might want to get a very new phone (aka factory reset) or just update yours. If you do NOT want to reset, be ready to have a BIG miscro-sd card which will hold all your data. while we repartition the phone.
Your microsd card must be be formatted such that it has an mbr and a partition. It is usually like that nowadays but if not, change it to have an mbr.
In other words this card in linux on a pc should be seen as /dev/mmcblk0 and its partition as /dev/mmcblk0p1. If you do not see the later, create mbr and a partition anew.

Now boot into the recovery image and see tiny (sorry) text instead of an ANDRO-logo. You can use adb now! and you MUST!

adb shell

It is immediately root.

BE CAREFUL!!! IT IS THE PROPER ROOT!!! NO LIMITS!!!

You have busybox (with all links), gdisk, sgdik and mksh in /sbin folder. It is a good linux recovery set of tools. Also you have some scripts in /rbin.
/rbin is NOT in your path so you will not run scripts from there unintentionally.

Go into /rbin

cd /rbin

scripts are for you and the ARE dangerous. So, follow instruction.

bu_... scripts backup your files to your sdcard (hope, you put it in vefore :) )

rr_... scripts restore your files from backup

flash_... scripts flash (see below what exactly)

.

OPTION 1. NO FACTORY RESET

run

./bu_data.sh

now you have all files from userdata and from GROW on your sdcard in a very fixed folder. Run gdisk, simply

gdisk

since /sbin is in your PATH.

Unfortunately, I cannot provide you help here as is solely up to you HOW you want to breakdown partitions. Just for reference, originally the partitions of interest reside as

  13         2818048         4456447   800.0 MiB   8300  userdata

  14         4456448        13565951   4.3 GiB     FFFF  GROW

where start and end are in 512-byte-sectors. I did them like

  13         2818048        13303807   5.0 GiB     8300  userdata

  14        13303808        13565951   128.0 MiB   FFFF  GROW

You achieve this in gdisk by deleting a partition and recreating it again with new boundaries. Remember to put proper flag (8300 or FFFF as before).

Once created AND WRITTEN, do not forget the command w to write your changes, you MUST reboot. it is the only way to instruct the kernel to read new partition table. Do it via

adb reboot recovery 

from your PC!!!

.

After the reboot again do

adb shell

you are back to your phone which has new partition layout but NO filesystems on those altered partitions. For GROW simply issue

mkfs.vfat /dev/block/mmcblk0p14

inside your phone, of course.

userdata needs more efforts. There are 2 ways to format it: use the stock recovery program which is there, or create a file-system on your pc.

Using recovery: start it by pressing vol-up then col-down on your phone. find the item "factory reset" and choose yes. This in fact does not reset anything but just formats userdata.
However, it also formats the partition number 31. It does not reboot after, so just continue to "restoring files".

You may see an error about llseek (95). Ignore it and read my posts on xda thread about if you wish.

!!!Technically all user installed programs are in userdata. I have no clue whether it is essential or not, this 31st partition. I have not traced its usage during the normal operation.
If you believe that formatting that partition will make a reset effect on reboot, do not use the recovery-program method!!!

Other way is to create the filesystem on your pc, so go there. create a file

dd if=/dev/zero of=your-file bs=512 count=EXACT

where EXACT=(end sector of your userdata partition - first sector of userdata partition +1) Now do

sudo mkfs.ext4 your-file

gzip -9 your-file

adb push your-file.gz /tmp

return into your phone and do

cd /tmp

gzip -c your-file.gz | dd of=/dev/block/mmcblk0p13

WAIT ABOUT 20 MIN if your partition is 5GB, do not worry.

.

Restoring files

Now restore your files using

cd /rbin

./rr_data.sh

Now all your files unpacked pack, like nothing have happened! The recovery program is still active: you can choose the reboot option there or say on your pc

adb reboot

.

.

FLASHING BETTER BOOT IMAGE

Since you are now booted inside your normal environment, choose your way to place the boot image and build.prop files from the /boot folder here on your sdcard EXACTLY in the folder
brnects0.715

cp kas.boot.bin build.prop /path/to/your/sdcard/brnects0.715

Be sure your sdcard in your phone now and issue on your pc

adb reboot recovery

It is just simpler than holding vol-down button :) go inside your phone 

adb shell

and then do

cd /rbin

./flash_boot.sh

This will first copy your present boot image under the name boot.bin in brnects0.715 folder on your sdcard and then flash kas.boot.bin in place

One more thing to tinker NOW, still on your phone:

mount /dev/block/mmcblk0p12 /system

mount /dev/block/mmcblk1p1 /mnt/extsd

cd /system

cp /mnt/extsd/brnects0.715/build.prop .

chmod 644 build.prop

cd /

umount /system

umount /mnt/extsd

Now your new image and some additional properties are in place: What exactly is different here compared to stock:

1. This image is composed of the kernel taken from recovery and a ramdisk taken from the stock image and altered

2. ro.secure=0 in the ramdisk

3. in init.rc file which guides the init process bootanimation and debuggerd services are disabled

4. also in the build.prop file which we placed additionally in /system att.service.entitlement=false (so you can tether) and service.adb.root=1 is set. Not sure that latter is essential.

.

.

OUTLOOK

Naturally, this recovery can be used to tinker the system, it is independent. Even if you mess up, you can restore everything. All tools are there and even extra can be uploaded
using adb. This way you can put su binary inside /system/bin. I'll put instructions later.

.

.

To be continued
