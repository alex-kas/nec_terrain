*You can find [here](exploit-pre.md) what are the mandatory pre-requisits for the exploit.*

---

### New recovery

#### What is new?

To understand what is *new* let's say what was *old*. The stock configuration of NEC Terrain comes with the ability to boot into the *recovery* mode. One of the purpose is to perform the *factory reset*. To be more specific let's explain. There are five partitions of the internal memory whihc you 'feel' working with this phone:
* `system` - where all the system pre-insatlled programs are
* `userdata` - where all the user insatlled programs go
* `GROW` - where all user files like photos and video go
* `boot` - image for the normal boot
* `recovery` - image for the recovery boot

*factory reset* means formatting `userdata` to ext4 and `GROW` to vfat using the stock `recovery` binary inside the recovery partition. All other partitions are considered immutable. It means that if you achieve eventually root and then mess up, say, `system` which is whatever inside the directory `/system`, you are in stuck. Stock recovery will not repair this.

Thus the wish is to implement a fully independent and fully functional recovery. Such that it would be capable to restore whatever in the system. This is also essential to repartition your system as originally you have almost no space for your programs (800MiB in `userdata`) and more than 4GiB just for photos, video, etc (in `GROW`).

#### Installing new recovery

* **recovery/** - folder: the proper recovery image is there

To install new recovery into its proper place, i.e. recovery partition, You download `adbr.sh`, `flash_recovery.sh`, `run_root_shell`, `sgdisk` and one of the `.bin` images from the `recovery/` folder here into one folder on your pc. Check that `run_root_shell`, `sgdisk` and both `.sh` scripts have permissions `755`.
**IMPORTANT:** whatever image you download you **must** save it under the name `kas.boot.bin` locally on your pc.

Now boot your phone normally, into its canonical stock boot configuration. Connect usb cable. Start `adb` daemon for exmaple by
```
sudo adb devices
```
Then execute on your pc (you should be inside the folder where you have just downloaded the stuff)
```
./adbr.sh
```
As the result you will have a brand new recovery image to be booted with *vol-down+power* pressed.

---

*You should proceed [here](boot-howto.md) for the next exercise: new boot image.*
