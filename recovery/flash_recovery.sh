#!/system/bin/sh
# remapping recovery partition to a standard hole
/data/local/tmp/sgdisk -d 11 /dev/block/mmcblk0 #deleting
/data/local/tmp/sgdisk -n 11:557056:589823 /dev/block/mmcblk0 #re-creating
/data/local/tmp/sgdisk -c 11:recovery /dev/block/mmcblk0 #naming
#/data/local/tmp/sgdisk -t 11:FFFF /dev/block/mmcblk0 -v
# flashing recovery
/system/bin/dd if=/data/local/tmp/kas.recovery.bin of=/dev/block/mmcblk0 bs=512 seek=557056 #flashing
/system/bin/sync #syncing
exit 0 #exiting

