*You can find [here](boot-howto.md) how to install the new boot image.*

---

### Repartitioning `userdata` and `GROW`

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

---

*You should proceed [here](debloat-howto.md) for the next exercise: debloating.*
