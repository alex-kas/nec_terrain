#!/bin/bash
adb push run_root_shell /data/local/tmp
adb push sgdisk /data/local/tmp
adb push kas.recovery.bin /data/local/tmp
adb push flash_recovery.sh /data/local/tmp

adb shell chmod 755 /data/local/tmp/run_root_shell
adb shell chmod 755 /data/local/tmp/sgdisk
adb shell chmod 755 /data/local/tmp/flash_recovery.sh

adb shell /data/local/tmp/run_root_shell -c "/data/local/tmp/flash_recovery.sh"
exit 0
