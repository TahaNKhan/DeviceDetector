# Device Detector

## What?
Detects a device on the local wifi network and beeps if a device name is listed in the "AlertOnDeviceConnectedList.txt" file.

## How?
1. Grabs the list of local devices' IP addresses from "arp -a" command in windows.
2. Runs the IP addresses through python's `socket.getfqdn(...)` function to get the host name.
3. Lets out a little beep noise if a devices listed in the `AlertOnDeviceConnectedList.txt` is found.
4. Keeps track of connected devices, so only alerts if the device was recently connected.

## Why?
I wanted to brush up on my python skills and found this idea on a youtube video.

## Future
1. Make the code cross-platform.
2. Allow configurable beeps/sounds for different devices in the list.

## Other Notes
1. Requires Python 3.9.
2. Needs elevated permissions to clear arp cache.