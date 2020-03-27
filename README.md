# pi_scripts

I need to add some documentation so my future dumb self knows what's going on. These are some hacky scripts that I use for my current raspberry pi B (version 1?) that I have mounted on my wall with 2 switches.

Currently the peripheral hardware is as follows

- Wifi dongle
- 1 SPST Wired up
- 1 SPDT Unconnected

In the future I want to maybe add the following

- Wiring up the SPDT switch
- 4 Regular LEDs
- 1 Connection to a custom peripheral board for an LED Strip

## Scripts

There's 3 main scripts in this project (and an abandoned directory that I used to do stuff with a usb camera).

### `ip_update.py`

This script simply grabs the local IP and the public IP and throws it into a google doc of mine every hour using IFTTT. The rate needs to be limited so as to not violate the number of requests one can make either daily or monthly (I forget the exact details).

The intention initially was to be able to SSH into this device from whereever. If I set up the port forwarding properly, but I don't think I've really taken advantage of that for some time.

### `monitor.py`

This is a really hacky script to post the system performance into a webpage I could access simply. Back when the deprecated camera stuff was in place I wanted to see what rates would affect the system to the point it'd fall over. Still kind of a neat page, and I could add stuff in the future to monitor other aspects of the system?

### `light_switch.py`

This is the meat of the system. Currently all it is looking for is the switch position and will send an IFTTT signal to turn on or off my light in my room.

I want to extend the functionality of this switch with additional peripherals mentioned above.

The second switch I would like for one position to indicate to hold the current RGB light values, and the other position to indicate to cycle through my preprogrammed colors.

Finally I'd like to add 4 LED's which I would use to indicate the last byte of my local IP address, so this way I wouldn't even need the up_ipdate script above.

## `rc.local`

This file as documented within the file itself resides in the `/etc/rc.local` and I can simply copy this file whenever I intend of adding scripts or removing them. The scripts above will automatically start on start up of the system.
