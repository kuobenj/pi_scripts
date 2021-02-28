# pi_scripts

I need to add some documentation so my future dumb self knows what's going on. These are some hacky scripts that I use for my current raspberry pi B (version 1?) that I have mounted on my wall with 2 switches.

Currently the peripheral hardware is as follows

- Wifi dongle
- 1 SPST Wired up
- 1 SPDT Wired up
- 1 Custom LED Strip

In the future I want to maybe add the following

- 4 Regular LEDs? Maybe there might be current issues.

## Scripts

There's 3 main scripts in this project (and an abandoned directory that I used to do stuff with a usb camera).

### `ip_update.py`

This script simply grabs the local IP and the public IP and throws it into a google doc of mine every hour using IFTTT. The rate needs to be limited so as to not violate the number of requests one can make either daily or monthly (I forget the exact details).

The intention initially was to be able to SSH into this device from whereever. If I set up the port forwarding properly, but I don't think I've really taken advantage of that for some time.

### ~~`monitor.py`~~

~~This is a really hacky script to post the system performance into a webpage I could access simply. Back when the deprecated camera stuff was in place I wanted to see what rates would affect the system to the point it'd fall over. Still kind of a neat page, and I could add stuff in the future to monitor other aspects of the system?~~

I've removed this from the rc.local file.

### `light_switch.py`

This is the meat of the system. Currently it is looking for is the switch position and will send a curl requet to turn on or off my light in my room.

The second switch holds the current RGB light values, and the other position to indicate to cycle through my preprogrammed colors.

~~Finally I'd like to add 4 LED's which I would use to indicate the last byte of my local IP address, so this way I wouldn't even need the up_ipdate script above.~~
I think actually the ammount of current draw may be too high for this functionality. It seems like each GPIO pin on a Pi can draw 16mA, but a regular red LED draws about 0.20mA, I think though there are some tutorials where one can further limit the current by using a larger resistor so this may be an option in the future.

## `rc.local`

This file as documented within the file itself resides in the `/etc/rc.local` and I can simply copy this file whenever I intend of adding scripts or removing them. The scripts above will automatically start on start up of the system.
