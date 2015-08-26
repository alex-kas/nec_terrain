#!/bin/bash
adb push run_root_shell /data/local/tmp
adb push sgdisk /data/local/tmp
adb shell '/data/local/tmp/run_root_shell -c "sgdisk -p /dev/block/mmcblk0"'
exit 0
