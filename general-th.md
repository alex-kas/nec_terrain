### Exploiting in general

#### Introduction

We are sepaking about Android phones (devices in general). These are run using the Android oeprating system and in reality 
are slim computers rather than just "phones". Most canonically such devices are locked by the manufacturers
from being tweaked. Not sure I understand the reason. Most likely makers afraid to loose something on the market.
You are therefore initally limited by some predefined functionality and some predefined installed programs.

Just several things which you **cannot** do by default on most (or prehaps all) phones:
* install custom operating system or at least custom system components
* remove bloatware (programs supplied with the phone and which have almost no use, but still eat resourses)
* enable blocked features, often tethering is blocked for commercial reasons. Tethering means your phone uses mobile data
to communicate with internet but serves for you as a wi-fi hotspot. So you can connect your laptop to the internet as well
* upgrade to newer versions of Android if the maker does not provide an update
* fix bugs in the system if the model is discontinued
* fix oddities which are not bugs but make the life difficult (like awful partitioning of the internal memory of NEC Terrain)
* Some other aspects as well

In order to overcome the limits and break-free you have to gain the control over the whole system. Some people name it
"rooting" but this is not always the best word.

#### A bit about the Android

Android is essentially linux with the user-interface programs written in java. Those programs are run by the java virtual machine.
What most people think about when they say Android is just that
graphical interface made by java programs.
However, if you want to go inside and manipulate the system of your phone you should understand basics of linux.
It is therefore a great plus for you if you are common with linux already.

The core of linux is its kernel - program code which initiate the system and which communicates between user and hardware devices.
It manages, apart from other devices, disks, file-systems, reading/writing of files.
It of course manages memory and processes in it. What is also essential, it checks permissions. What which user can
and cannot do.

The main user has identifier 0 (zero) and is traditionally named `root`. Traditionally it has full access to everything.
However, this is not obliged to be, and in NEC Terrain in particular it is not!

#### Usual types of defense which makers use

As much as possible makers of the phones and tablets, as well as carriers, try to protect devices from being altered. They explin this by their worry that you can damage the device. In some cases they preserve their commercial interests but in many instances a paranoic defense is unexplainable.

##### No *root* access

Traditionally, if you are the `root` you have full access. Kernel permits it. So, in order to avoid this all processes are being run *not* as `root`. So, you simply cannot execute many system-level commands. To become the `root` you must have a special program, usually named `su` which changes your status to `root` provided a proper configuration file is arranged. Looks simple, just download this program and run it. BUT, the system does not allow you to write it into the directory with programs, like `/system/bin`. Moreover, it does not allow you to run programs from other locations. You are kind of in stuck. Still, usually, `/data/local/tmp` is a place where programs can be run but it is not convenient, as this directory is not in the search path. You have to type all way down `/data/local/tmp/su`

However, let's comment on *traditionally*. Traditionally means that the kernel behaves as follows. Consider mounting of `/system` partition as an example. The pseudo-code maybe like that:
```
start mounting function
if (used_id!=0) return ERROR_NOT_PERMITTED
<continue>
```
Imagine other code:
```
start mounting function
if (partition=="/system") return ERROR_NOT_PERMITTED
<continue>
```
You see, in the second case `/system` cannot be mounted whoever you are. Full stop. No way. Even if you are `root`

So, being `root` does not mean be allowed everything. Traditions may be broken. This is exactly what hapens in NEC Terrain with the stock kernel when you boot normally. Luckily, the recovery boot of this phone has a *different* kernel, free of such security locks. As you can imagine, one of the futher step will be to stuff the normal boot with the kernel from recovery.

##### Locked bootloader

This is another *feature* used by phone makers. The boot process goes in stages. Program code from various partitions of the internal memory is being executed in order. During this the phone initialization is performed. After many really initial stages the so called `aboot` is executed. This guy decides what to boot: *normal* or *recovery* mode depending on has or not the *vol-down* key been pressed. Then it boots using either `boot` or `recovery` partition.

The trick is that before `aboot` is called it is being checked using certificates written inside and computing the hash sum. If the check does not succeed the boot process halts.

In the same manner `aboot` check `boot` or `recovery`.

This is way more complicated proble to overcome than just become a `root`. The oddity is as follows. Once you have become the `root`, you may have chances to overwrite, say `boot` partition with your new lovely kernel, but this kernel may **not** be booted by `aboot` becuase its hash is wrong.

This is not just a mistake, this with high probability a complete **brick** out of your phone. You therefore must be absolutely sure **before** altering bootable partitions, that this is in accord with possible lock mechanisms.

##### NAND-lock

This is the most strange concept for a normal pc user like me. Essentially it means nothing. The term NAND originates from the technical name of the memory organization type on a chip. *NAND-lock* means some way of preventing writing to the internal memory. However, if you are common with pc you understand that in principle there are only three ways of such a lock.

1. Physical lock by some physical switch, like on sd-card. Easy to find and maybe impossible to unlock. Stop.
2. *Collaborative* lock. For example, some byte, somewhere is set to 1 and than the kernel, understanding this, prevents writing. Whould that byte be '0', the kernel would allow writing. I.e. the kernel *collaborates* on some pre-arranged convention. It is like a region lock on a dvd. Standard dvd-drive would refuse disks from a wrong region. The disk can be read but the drive simply does not want to read it. You can easily change this by reflashing the dvd-drive firmware. To remove such type of lock you must trace it down and find out the beast. I.e. break the convention.
3. The most tricky - *man-in-between*. Like a resedential program in old ms-dos or like a hypervisor. It means that before you system kernel is loaded some pre-kernel is injected into the memory. It serves as the relay between the full system kernel and the internal memory chip. When the system kernel issues the write request, this request is being captured and checked by the pre-krenel. If, for instance, the request addresses an arrea to be protected, such a request is blocked. Being tricky such a lock means that you must find and change the pre-kernel.

All these locks can be effectively used to prevent you from writing new data somewhere. Again, on NEC Terrain, even if you are a `root`, you cannot override, for instance, `boot` as the kerel prevents such attempts.

#### What to do in general?

As we have seen, several defenses are used. They are complementary. Being root does not neccessarily mean you can override bootable partitions, for example. Or, being root does not mean you can safely change bootable partitions. Thus, to tame the phone completely you must arrange three things:
1. Become sure that replacing bootable partitions will not brick your device. Or path a way to prevent this.
2. If you cannot override bootable partitions, find a way to remove the write-lock
3. When you succeeded in two previous points, arrange such a `root` access that you can really write a program like `su` in a proper place like `/system/bin`

Now we are ready to go for NEC Terrain.

---

*You should read [here](exploit-th.md) about the theory of exploiting NEC Terrain.*
