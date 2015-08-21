*You can find [here](boot-howto.md) how to install the new boot image.*

---

### Repartitioning `userdata` and `GROW`

Re-partitioning  is a straightforward but a *must-to-be-done-accurately* procedure. Mistakes may cost you a phone.

**The micro-sdcard must be IN the phone!**

**The new recovery must be installed!**

Boot into the new recovery with *vol-down+power* pressed. Start the `adb` daemon on your pc, for instance doing
```
sudo adb devices
```
Go into the shell
```
adb shell
```

#### Step 1. Backup.

Skip it if you do not care neither about your files nor about settings or programs installed by you and (therefore) want an effect of *factory reset*

If you care about something of the above - do backup. It is as follows (commands inside the adb shell)
```
cd /rbin
./bu_data.sh
```
You will see a long output listing each file added to an archive on your sdcard in a very special folder `brnect08.715`

#### Step 2. Actual re-partitioning

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

All modifications are in **memory**! It is safe, but **do not forget to write**, using command **w** before you quit.

* **?** - anytime for help
* **d** - delete partition, it asks number: enter number and press `enter`
* **n** - create new partition, it asks number. If say, you deleted partition number 14, you now can enter 14, so you will just redo it, but of another size. Then starting and ending sectors are asked. You can just get from the table above. OR invent YOURS! As you like. Then it asks about a flag, agree to 8300, even for GROW. Standartly FFFF flag is not supported
* **c** - **CRUCIAL**: you **MUST** give it a name as it was before, **EXACTLY**. Before entering the name you will be asked the partition number, of course
* **p** - print, how the table looks now
* **w** - write changes to disk, w/o this you will loose your efforts!
* **q** -- quit

Once created **and written** by issuing the command `w` INSIDE `gdisk` you **MUST** reboot. It is the only way to instruct the kernel to read new partition table. Do it from your pc (*not* from the shell) via
```
adb reboot recovery 
```
After the reboot you are back to the recovery environment.

#### Step 3. Formatting

Go into the shell by typing on your pc
```
adb shell 
```
Now you **must** create file-systems on your re-shuffled partitions (command inside the adb shell)
```
mkfs.vfat /dev/block/mmcblk0p14
mkfs.ext4 -b 1024 -i 4096 /dev/block/mmcblk0p13
```
You are kindly instructed to write the arguments for the ext4 formatiing exactly as they are here. These values of `-b` and `-i` will save you from vasting 25% of the `userdata` space for *nothing*!

After this you will have a system *exactly* like after a stock *factory reset*.

##### Step 4. Restoring your files

Skip it if already skipped the step 1 or if you have changed your mind and want an a la *factory reset* phone.

To restore your files issue inside the adb shell
```
cd /rbin
./rr_data.sh
```
This will unpack all your files from the backup into the previous place like nothing has happened!
Now exit the shell
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
