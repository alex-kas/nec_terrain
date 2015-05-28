# nec_terrain
Exploiting NEC Terrain mobile

The pre-story can be found in http://forum.xda-developers.com/showthread.php?t=2515602
and some very useful scripts can be found in https://github.com/x29a/nec_terrain_root.

Current files:

boot/ - boot kernel

recovery/ - recovery kernel and the recovery binary

In short: it is a great qwerty phone which is crazily locked from any known rooting attempt.
What is known so far is how to get temporary root at the user level, how to disable a lot of
bloatware and how to pull the raw images of all internal partitions. The practicalities are
collected in the x29a's github "nec_terrain_root".

The main problem is that the phone is nand-locked, so no straight approch to replace the rom.
However, as we can imagine, the phone itself allows recovery and upgrade possibilities.
Those options MUST clear the nand-lock to accomplish the task. Oddly, entering the recovery mode
(by switching on with the vol-down pressed) is not enough. The desired options of "sdcard recovery"
and "maintanence" are locked by an unknown password. Neither NEC nor AT&T opens the cards.

So, in principle, we have to hack the recovery password or try to force the recovery process bypassing the recovery utility developed for this phone. Below are my findings for the moment:

Thanks to x29a I have extracted partitions smoothly. BTW, the relevant script get_partitions.sh at least on my box needs a microfix: numbers 1-9 should be 01-09. Anyway, the story is like that:
1. There are two nice partitions: boot and recovery, numbers 9 and 11 respectively. Both are android bootables with a kernel, ramdisk and some garbadge (or maybe the place for passwords?). Oddly, kernel is not aligned at 2k as android prescribes but still things are extractable. Kernels are DIFFERENT, while sizes are identical, both things are for no obvious reason. The aligment offset of both kernels is the same though. It is 0x4899. Perhaps, these are not exactly kernels but rather some portions of partitions while the full story is more involved:
I first found the gzip magics, one at 0x4899 and one way below. Then, following the standards, I said that the kernel is the peace in between of the first and the second gzip magics. I gave this to gzip and it accepted to unzip saying that the trailing garbage is ignored.
What is incredible, that the sizes of both kernels AFTER gunzip are identical. How come?
2. I retrieved all files from both ramdisks. Structures of ramdisks are similar but the content is different. In particular the boot partition ramdisk has adbd in /sbin. recovery ramdisk has RECOVERY in ramdisk.
3. I bet 200% that this RECOVERY program, /sbin/recovery, is responsible for requesting the maintenence password. 400%. It is there! BUT, it is binary (ARM ELF) where only strings of data are easily accessible (among these strings there are those which you exactly see in <3e> mode, that is why I bet with confidence).
4. This recovery file seems to be based on original recovery.c from google (https://android.googlesource.com/platform/bootable/recovery/+/fadc5ac81d6400ebdd041f7d4ea64021596d6b7d/recovery.c) but stuffed by NEC-API with the support of FOTA (firmware on the air) and this f***g password lock.
5. At this stage we need a decent disassembler for ARMv7 with Krait cpu to understand: WHAT HAPPENS WHEN ONE PRESSES <OK>?

The recovery binary is JUST 500k, the whole recovery partition is just 10M. The problem seems to be narrowed significantly.

Theories:
1. The password is hardcoded in the binary. But then it should appear somehow either in .data or in .rodata sections of ELF. From the first look it is NOT there, but who knows for sure?
2. The password is in a separate file but the only strange reference is for /cache/trace/sndata.bin (BTW, cache is one more partition among sevral mounted from /etc/recovery.fstab, it is just ext4). In general this cache partition has some logs, also about previous installs. The file sndata.bin is there, it is 15 bytes, semi-binary, but its creation date was as the date I have copied my phone partitions. Not sure it is the true place, and how one would convert 14 bytes to 10 digits? Again a problem, if it is here, but other level of difficulty (simpler).
3. The password is hardcoded in the ramdisk at a specific location and is read by direct disk access method. For this one should be common with arm architecture a bit deeper than a newby.
4. The password is hardcoded somewhere else, and again is read by the direct disk access techinque.
5. None of the above: then ...

Some hints:
1. In <3e> mode you can WIPE the cache partition. WITHOUT any password. I wiped mine! Surpirsingly, I observe all files I saw there before including the sndata.bin. Its timestamp has been renewed. Moreover, its content is the same.
2. The portions of boot and recovery partitions before kernels are very similar but NOT the same. This in principle may be a place for a password.

The main problem now is at least to identify the place in the binary where the recovery program starts working out the password input.

Interesting move has been suggested by user rpadula at xda-developers thread. Try to use KEXEC. It is not known whether we can do so using the temporary root, because the root itself is not enough. The kernel must be comiled such that is allows kexec call.
If one can use kexec, then there are 2 possibilities:
1. If the nand-lock is released by the recovery kernel, then we take as the kernel the recovery kernel and the recovery ramdisk image modified via replacing the NEC's recovery by a normal recovery.
2. If the nand-lock is released by the recovery utility itself just before the actual update, than we need its password, again.
 
Another possible shot worth tryin is like that. If the recovery kernel releases the nand-lock then during the <3e> inital screen the nand is unlocked. If I reboot by using menu or button, it locks again, this I'm sure, but if I take off the battery ... Moreover, if the normal boot kernel does not check for this then I have the nand unlocked! ... TOOOOO many ifs but why not to try?

Suggestions are welcome :)
