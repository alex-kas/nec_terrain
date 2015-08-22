### NEC Terrain boot image

This boot image is made of a kernel extracted from the stock recovery and a modified original ramdisk from the boot image. This kernel does not
enforce a write-protection above linux permissions and privileges.

* `kas.boot.bin-vvv` - the boot image, version vvv
* `build.prop` should be placed in the `/system`

* `adbb.sh` - script to place the boot image and build.prop in a special folder on the sd-card (`brnects0.715`) so that a script in recovery `/rbin/flash_boot.sh` can see them and write in place.

#### Changelog for the *image*:

* **version 0.9** (`kas.boot.bin-0.9`)
  * service flash_recovery is commented out to prevent a possible FOTA action
  * service pmeval is commented out as its binary does not exist
  * service ms-monitor is commented out as its binary does not exist
  * service immvibed is commented out as its binary does not exist
  * insertion of the module adux1001_driver.ko is commented out as it does not exist
  * insertion of the module tspdrv.ko is commented out as it does not exist

* **version 0.8** (`kas.boot.bin-0.8`, the very first!)
  * kernel from the stock recovery  
  * ramdisk/default.prop: ro.secure=0, no obvious use
  * ramdisk/init.rc
    * All mtd@xxx attempts removed
    * e2fsck enforced on `/system` (partition 12) as it can be writable now
    * `noauto_da_alloc` removed on mounting /data (partition 13)
    * All ext4 partitions are mounted with `noatime,nodiratime,discard` instead of `relatime`
    * Service `debuggerd` disabled
    * Service `bootanim` (bootanimation) disaled
  * ramdisk/init.target.rc: `/tombstones` (partition 17) is now mounted with `noatime,nodiratime,discard` instead of `relatime`
  * /system/build.prop
    * att.service.entitlement=false for tethering
    * service.adb.root=1 added, no obvious use
  * **negative**: setting ro.debuggable=1 in ramdisk/default.prop leads to starting 2 additional services from ramdisk/init.rc **discarded**
  * **negative**: setting ro.build.type=eng in /system/build.prop leads to flashing red border during the phone operation. **discarded**

* **version -1** (stock)
