adb push run_root_shell /data/local/tmp
adb push sgdisk /data/local/tmp

adb shell chmod 755 /data/local/tmp/run_root_shell
adb shell chmod 755 /data/local/tmp/sgdisk

adb shell /data/local/tmp/run_root_shell -c '/data/local/tmp/sgdisk -p /dev/block/mmcblk0'
