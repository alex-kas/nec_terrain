#!/bin/bash
adb shell "mkdir /mnt/external_sd/brnects0.715"
adb push kas.boot.bin /mnt/external_sd/brnects0.715
adb push build.prop /mnt/external_sd/brnects0.715
exit 0
