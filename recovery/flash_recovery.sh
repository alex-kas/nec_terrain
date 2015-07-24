#!/system/bin/sh
# remapping recovery partition to a standard hole
/data/local/tmp/sgdisk -d 11 /dev/block/mmcblk0
/data/local/tmp/sgdisk -n 11:557056:589823 /dev/block/mmcblk0 -v
/data/local/tmp/sgdisk -c 11:recovery /dev/block/mmcblk0 -v
/data/local/tmp/sgdisk -t 11:FFFF /dev/block/mmcblk0 -v
# flashing recovery
/system/bin/dd if=/data/local/tmp/kas.recovery.bin of=/dev/block/mmcblk0 bs=512 seek=557056
/system/bin/sync
exit 0

