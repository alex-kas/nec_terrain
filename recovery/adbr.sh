#!/bin/bash
adb push run_root_shell /data/local/tmp
adb push kas.recovery.bin /data/local/tmp
adb shell '/data/local/tmp/run_root_shell -c "dd if=/data/local/tmp/kas.recovery.bin of=/dev/block/mmcblk0p11"'
adb shell '/data/local/tmp/run_root_shell -c "sync"'
exit 0
