#!/usr/bin/env
./droneupload.py
cd /Volumes/Drone/DCIM
scp -r * nathan@ubuntuServer:/media/NAS/nathan/Drone
rm -r *