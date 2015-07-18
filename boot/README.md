### NEC Terrain boot image

This boot image is made of a kernel extracted from the stock recovery and a modified original boot image. This kernel does not
enforce a write-protection above linux permissions and privileges.

`build.prop` should be placed in the `/system`

`adbb.sh` - script to place the boot image and build.prop in a special folder on the sd-card (`brnects0.715`) so that a script in recovery
`flsh_boot.sh` can see them. In fact now this script flashes only the image, `build.prop` must be put by hands.

#### Changelog:

* version 0.8 (the very first)
  * kernel from the stock recovery  
  * ramdisk/default.prop: ro.secure=0, no obvious use
  * build.prop
    * att.service.entitlement=false for tethering
    * service.adb.root=1, no obvious use
  * init.rc
    * All mtd@xxx attempts removed
    * e2fsck enforced on `/system` (partition 12) as it can be writable now
    * `noauto_da_alloc` removed on mounting /system
    * All ext4 partitions are mounted with `noatime,nodiratime,discard` instead of `relatime`
  * ramdisk/init.target.rc: `/tombstones` (partition 17) is now mounted with `noatime,nodiratime,discard` instead of `relatime` in 

* version -1 (stock)
