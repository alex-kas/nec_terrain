*You can find [here](repart-howto.md) how to repartition NEC Terrain.*

---

### Placing `su` and `Superuser.apk`

* **system/** - folder: the relevant files are there

You download from the `system/` folder here to some place on your pc:
* `adbs.sh (adbs.bat for windows)`
* `su`
* `Superuser.apk`

Ensure that your `adb` daemon is running bu issuing
```
sudo adb devices
```
**The new recovery must be installed!**

In linux check that `adbs.sh` has 755 permissions. To be sure simply issue from inside the directory where you have downloaded the files
```
chmod 755 adbs.sh
```
Now restart your phone into recovery typing on your pc
```
adb reboot recovery
```
From the directory where you have downloaded the suepruser stuff do
```
./adbs.sh
(adbs.bat [for windows])
```
Once done, reboot the phone by
```
adb reboot
```
After the reboot you will see "Android is upgrading" meaning it installs a new 'system' program `Superuser.apk`

---

*You may want to proceed [here](ts.md) for the troubleshooting hints.*
