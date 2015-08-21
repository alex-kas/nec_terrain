*You can find [here](recovery-howto.md) how to install the new recovery.*

---

### Placing new boot image

* **boot/** - the images are there

To install a new boot into its proper place, i.e. boot partition, you download `adbb.sh`, `build.prop` and one of the the `.bin` images from the `boot/` folder here to some place on your pc. Check that `adbb.sh` has `755` permissions.

**IMPORTANT:** whatever image you download you **must** save it under the name `kas.boot.bin` locally on your pc.

Your phone must be booted normally. The `adb` daemon must be started on your pc. To be sure in the latter issue, for instance
```
sudo adb devices
```
Run on your pc (you are inside the directory where you downloaded the files)
```
./adbb.sh
```
To copy files to a proper location on your sdcard (folder named `brnects0.715`), the card must be in the phone.

Now restart your phone into recovery typing on your pc
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
Comments: you first mount the actual system to the folder `/system`; then sdcard to the folder `/sdcard`; then you go inside of the system via `cd` and copy the `build.prop` file from sd card there (mind the final dot `.` in the `cp` command, it means the folder where you are *now*, `/system` in this case); then you change permission for `build.prop`; quit to the root folder `/`; and finally unmount mounted partitions using `umount`. The later step ensures all data which could be in cache are really written.

This is *the* way you should do **whatever** with your system next time.

Now
```
exit
```
to come back to your pc and
```
adb reboot
```
**DONE!**

---

*You should proceed [here](repart-howto.md) for the next exercise: repartitioning.*
