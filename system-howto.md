*You can find [here](repart-howto.md) how to repartition NEC Terrain.*

---

### Placing `su` and `Superuser.apk`

You can get `su` and `Superuser.apk` from the **system/** folder here. Then, in order to install them properly do the following commands. Ensure that your `adb` daemon is running bu issuing
```
sudo adb devices
```
**The new recovery must be installed!**

Boot the phone into the recovery mode by pressing *vol-down+power*. From the directory where you have downloaded the suepruser stuff do
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
After the reboot you will see "Android is upgrading" meaning it installs a new 'system' program `Superuser.apk`

---

*You may want to proceed [here](ts.md) for the troubleshooting hints.*
