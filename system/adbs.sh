#!/bin/bash
adb push su /tmp
adb push Superuser.apk /tmp
adb push flash_superuser.sh /tmp

adb chmod 755 /tmp/flash_superuser.sh

adb shell "/tmp/flash_superuser.sh"
exit 0
