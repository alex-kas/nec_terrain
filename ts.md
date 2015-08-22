*You can find [here](system-howto.md) how to tweak your system.*

---

### Troubleshooting

Interaction of your pc with the phone may stall. No clue why exactly but if you believe that some operation cannot last so long you can try to wake up `adb` either by
trying `adb shell` from another terminal on your pc or by unplugging/re-plugging the usb cable. In extreme case you may have to take the battery off, then place it back and then boot your phone
with *vol-down* pressed. (the latter happened to me only once).

Notice that some operations take indeed long time. Sometimes mounting of a partition takes up to 15 seconds. Again, no clue, why.
