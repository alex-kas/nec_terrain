## NEC Terrain

_As the name of the project suggests all the resources here are devoted to the NEC Terrain mobile phone. As such all
the resources here are specific to this phone (even though theoretically applicable to another one). Moreover, various subjective statements reflect my **personal** opinion._

### Specifications and goods

To be more precise we are talking about the following phone (the info from the `about` menu inside the phone):
* Model number: NE-201A1A
* Android version: 4.0.4
* Baseband version: N126400001
* Kernel version: 3.0.8 ncmc@ncmc #2 SMP PREEMPT Thu Sep 26 17:01:21 IST 2013
* Build number: 126460101

and the full specifications can be found [here](http://www.gsmarena.com/nec_terrain-5553.php).

In short, this is a heavily protected phone, all-proof (water, dust, salt, ...) with QWERTY physical keyboard which is also water-proof. You can type under the rain. It is reasonably fast: 1.5GHz dual-core CPU and it even has 1GB of RAM. The stock configuration has Android 4.0.4. Its internal memory is 8GB. Seems like a unique combination in the world of all phones.

In fact the king property is the physical keyboard. If someone wonders why: the physics of a touch screen is such that its functionality is almost absolutely screwed up in a presence of water-drops. Under the rain or a wet snow, or if your fingers are wet. You are just unable to operate a phone w/o a keyboard in such conditions.

Leaving the keyboard aside, this phone is comparable to Samsung Galaxy S4 Active or even outperformed by Casio Commando 4G LTE, Samsung Galaxy S5 Active and Samsung Galaxy S6 Active. However, my life-style demands the physical keys to be.

### Odds

This phone has several serious odds:

* It is discontinued. No updates are expected even though the phone itself is capable for KitKat at least
* Its partition scheme is as awful as that:
  * 800MiB for programs installed by you. Practically nothing, just updates to the system apps get it all immediately
  * 4.3GiB for your files, like photos, video, but *not* programs
* Tethering cannot be enabled
* A bug (one so far) was found which brings the phone to reboot if a program needs to read big set of data files

The less severe problem is the big amount of bloatware.

### Table of contents

1. [General theory](general-th.md) - is a worth reading text which explains what is rooting, nand-lock, bootloader unlocking, and why these are different and sometimes disconnected things. Also many terms are explained there.
2. [Exploit](exploit-th.md) - explains the theory of how the NEC Terrain is exploited
3. [Pre-requisits](exploit-pre.md) - lists mandatory pre-requisits to exploit the NEC Terrain
4. [New Recovery](recovery-howto.md) - desciption of the new recovery image and a step-by-step instruction to install one
5. [New Boot](boot-howto.md) - description of the new boot image,  a step-by-step instruction to install one
6. [Re-partitioning](repart-howto.md) -  a step-by-step instruction to re-partition the internal memory
7. [System modification](../blob/master/system-howto.md) -  several useful howto-s on system modification
8. [Debloating](system/README.md) - lists of apps which can be disabled and why, and which *cannot* be disabled and why



#### Troubleshooting

Interaction of your pc with the phone may stall. No clue why exactly but if you believe that some operation cannot last so long you can try to wake up `adb` either by
trying `adb shell` from another terminal on your pc or by unplugging/re-plugging the usb cable. In extreme case you may have to take the battery off, then place it back and then boot your phone
with *vol-down* pressed. (the latter happened to me only once).

Notice that some operations take indeed long time. Sometimes mounting of a partition takes up to 15 seconds. Again, no clue, why.
