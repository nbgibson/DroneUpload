#!/usr/bin/env python3
import datetime
from datetime import datetime
import os
import sys

osPath = "/Volumes/Drone/DCIM"

# Verify the SD card is present


def SanityCheck():
    if os.path.exists(osPath + "/100MEDIA"):
        pass
    else:
        sys.exit("Drone SD mount not found")


# Get and formate DateTime string for naming
def DTString():
    date_time = datetime.now().strftime("%y.%m.%d")
    return date_time

# Rename dir and files to yy.mm.dd per storage naming conventions


def RenameFiles():
    os.chdir(osPath + "/100MEDIA")
    for filename in os.listdir():
        print(filename.replace("DJI", DTString() + "_DJI"))
        nuName = filename.replace("DJI", DTString() + "_DJI")
        os.rename(os.path.join(os.getcwd(), filename), nuName)
    os.chdir("..")
    os.rename("100MEDIA", DTString())
    # os.mkdir("100MEDIA", 777) Removing for now to make the SCP portion a bit easier


SanityCheck()
