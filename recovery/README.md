### NEC Terrain boot image

This recovery image is made of the original kernel used in the stock recovery and an amended original ramdisk. This kernel does not
enforce a write-protection above linux permissions and privileges.

Images:
* `kas.recovery.bin` - the recovery image v0.8
* `kas.recovery_no.bin` - the recovery image v0.8.1, actually the same image with the recovery binary disabled; for those who is scared by a possible fota update

Install script:
* `adbr.sh` - script to be run on your computer to eventually flash the recovery image on a normally booted phone.

Required binaries and scripts for the install:
* `run_root_shell` is used to flash this image on a non-rooted NEC Terrain
* `sgdisk` is used to re-map recovery partition to a know standard hole
* `flash_recovery.sh` - the script which is run on the phone to do re-map of the partition and flashing

#### Changelog for the *image*:

* **version 0.8.1** (`kas.recovery_no.bin`)
  * ramdisk/init.rc: recovery binary disabled

* **version 0.8** (`kas.recovery.bin`, the very first!)
  * ramdisk/default.prop
    * ro.secure=0, no obvious use
    * ro.debuggable=1, no obviouc use
    * service.adb.root=1 addded, no obvious use
    * ro.build.type=eng, no obvious use
    * att.service.entitlement=false, no obvious use in this regime
  * ramdisk/init.rc: all stuff governing adb uncommented, not sure it plays role
  * ramdisk/adbd replaced with adbd insecure binary hacked for new placing of the shell sh
  * New files in ramdisk/sbin
    * busybox + all its symlinks
    * mksh - shell, slightly hacked for new placing of itself and mkshrc
    * mkshrc - rc file for mksh, has aliases
    * sh is symlinked to mksh
    * gdisk
    * sgdisk
    * mkfs.ext4 - very big, need smaller
  * New directory ramdisk/rbin
    * bu_ - scripts for data backup
    * rr_ - scripts for data restore
    * flash_ - scripts for flashing
  * Known bugs:
    * adbd stalls from time to time. Can be woken up by another shell request or by cable dis-/connect. Once led
    to the need of battery off/in

* **version -1** (stock)
