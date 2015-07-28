### Exploiting in general

#### Introduction

We are sepaking about Android phones (devices in general). These are run using the Android oeprating system and in reality 
are slim computers rather than just "phones". Most canonically such devices are locked by the manufacturers
from being tweaked. Not sure I understand the reason. Most likely makers afraid to loose something on the market.
You are therefore initally limited by some predefined functionality and some predefined installed programs.

Just several things which you **cannot** do by default on most (or prehaps all) phones:
* install custom operating system or at least custom system components
* remove bloatware (programs supplied with the phone and which have almost no use, but still eat resourses)
* enabled blocked features, often tethering is blocked for commercial reasons. Tethering means your phone uses mobile data
to communicate with internet but serves for you as a wi-fi hotspot. So you can connect your laptop to the internet as well
* upgrade to newer versions of Android if the maker does not provide an update
* fix bugs in the system if the model is discontinued
* fix oddities which are not bugs but make the life difficult (like awful partitioning of the internal memory of NEV Terrain)
* Some other aspects as well

In order to overcome the limits and break-free you have to gain the control over the whole system. Some people name it
"rooting" but this is not always the best word.

#### A bit about the Android

Android is essentially linux with the user-interface programs written in java. Those programs are run by the java virtual machine.
What most people think about when they say Android is just that
graphical interface made by java programs.
However, if you want to go inside and manipulate the system of your phone you should understand basics of linux.
It is therefore a great plus for you if you are common with linux already.

The core of linux is its kernel - program code which initiate the system and whihc communicates between user and hardware devices.
It manages, apart from other devices, disks, file-systems, reading/writing of files.
It of course manages memory and processes in it. What is also essential, it checks permissions. What which user can
and cannot do.

The main user has identifier 0 (zero) and is traditionally named `root`. Traditionally it has full access to everything.
However, this is not obliged to be, and in NEC Terrain in particular it is not!

#### Usual types of defense which makers use

##### No *root* access

##### Locked bootloader

##### NAND-lock

#### ToDo

The pre-story can be found in

http://forum.xda-developers.com/showthread.php?t=2515602

Many useful scripts, links and the unlocking app, **terroot**,  can be found in 

https://github.com/x29a/nec_terrain_root

The latter is an easily traceable app which implements the method presented here and outlined first in

http://forum.xda-developers.com/showpost.php?p=61542922&postcount=186 (also few posts before and all way down)

The bootable images used in **terroot** are from here as well.

#### Exploit terminology

* *boot* - normal boot via the image on the boot partition (number 9). The stock kernel in this image blocks read-write access to the vital system areas, i.e. system, boot, recovery, sbl1,2,3, aboot, rpm, tz partitions.
You cannot write there even if you are root. You moreover cannot remount those partitions rw. The physical area of the internal memory where these partitions are is also write-protected by the kernel.
* *recovery* - recovery boot (via *vol-down+power*) via the recovery partition (number 11). The kernel there turned out to be free of the write-blocks.
* *system* (or *ROM*) - your actual operating system, all inside `/system` directory

Each bootable image has kernel and the initramdisk to kick-off the system. In our story stock kernels in boot and recovery are different, clearly due to presence/absence of blockages but
the config.gz (the file containing parameters with which the kernel was compiled) for both kernels is identical.

In order to root the phone *permanently* we need to place the `su` binary inside `/system/bin` (or `/system/xbin`) and the goal is to open the latter directory for write. Since even root cannot do it, the new goal is to modify the boot
image where all mountings happen. But re-flashing of an image is not possible.

So, the goal is to flash a modified image to a new place and instruct the system about this.

#### GPT

* *GPT* - is the table which is located at the beginning of a disk and describes where on the disk each parition lies. A verification copy of the table is at the end of the disk. Those copies **must** match. Also some specific checksums inside these tables **must** be correct.

Two facts turned out to be true in this phone:

* Out of the sudden the gpt table itself is **not** protected from writing.
* There are holes between partitions.
* Those holes are **not** write-protected

Therefore, we can try to modify the table and change the position of a bootable partition to be inside a writable hole. Then write the new image there and try to boot it. However ...

#### Bootloader

The bootloader is located in the partition 7 on this phone. It is named *aboot*. The main danger is that sometimes bootloaders refuse to boot wrong images. Wrong means those w/o security keys or with a wrong checksum or both. In an extreme case the bootloader can in principle soft-brick your phone. I.e. write internally some data which indicate the attempt to boot a wrong image and refuse any further booting.

A detailed reverse-engineering of the boot locker showed however that it is just a joke. It exists, it check certificates, hash, etc, but its logic is like that:

1. If I see a wrong image I write one byte just inside my aboot image.
2. Then I boot your wrong kernel, so to say "have it".
3. Next time, if I see that the byte from point 1 above is set, I boot whatever you like w/o verification.
4. ...

Good for us, less work. As long as you can flash a modified image.

---

*You should read [here](exploit-pre.md) what are the strict requirements to implement the exploit.*
