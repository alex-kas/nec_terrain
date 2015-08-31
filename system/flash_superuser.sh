#!/sbin/sh

cd /tmp #workdir
mount /dev/block/mmcblk0p12 /system #mounting system
cp su /system/xbin/su #copying su binary
chown 0:0 /system/xbin/su #chown on su
chmod 6755 /system/xbin/su #chmod on su
ln -s /system/xbin/su /system/bin/su #ln to /system/bin
cp Superuser.apk /system/app #placing apk
chmod 644 /system/app/Superuser.apk #chmod on apk
umount /system #unmount system
exit 0 #exiting

