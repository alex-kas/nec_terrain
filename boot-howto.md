*You can find [here](recovery-howto.md) how to install the new recovery.*

---

### Placing new boot image

* **boot/** - folder: the images are there

To install a new boot into its proper place, i.e. boot partition, you download from the `boot/` folder here to some place on your pc:
* `adbb.sh (adbb.bat for windows)`
* `build.prop`
* one of the the `.bin` images. **IMPORTANT:** whatever image you download you **must** save it under the name `kas.boot.bin` locally on your pc.

In linux check that `adbb.sh` has `755` permissions. To be sure simply issue from inside the directory where you have downloaded the files
```
chmod 755 adbb.sh
```
Your phone must be booted normally. The `adb` daemon must be started on your pc. To be sure in the latter issue, for instance
```
sudo adb devices
(adb start-server [for windows])
```
**The microsd-card must be __in__ the phone.**


Run on your pc (you should be inside the directory where you downloaded the files)
```
./adbb.sh
(adbr.bat [for windows])
```
To copy files to a proper location on your sdcard (folder named `brnects0.715`).

**The new recovery must be installed!**

Now restart your phone into recovery typing on your pc
```
adb reboot recovery
```
Wait at least the 'NEC' logo. After the 'NEC' logo this recovery shows **NOTHING**. Now go into shell
```
adb shell
```
and do inside the shell
```
cd /rbin
./flash_boot.sh
```
It will copy the current boot image to sdcard as `brnects0.715/boot.current.bin` and flash `kas.boot.bin` into place. On top of this it places `build.prop` file found in `brnects0.715/` on sdcard into `/system`.
Now exit the shell
```
exit
```
to come back to your pc and reboot the phone
```
adb reboot
```
**DONE!**

---

*You should proceed [here](repart-howto.md) for the next exercise: repartitioning.*
