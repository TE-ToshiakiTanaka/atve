import os
import sys

from android_base import Android

class _07daed71(Android):
    SERIAL = "07daed71"
    TMP_PICTURE="%s_TMP.png" % SERIAL
    IP = ""
    PORT = ""

    NAME = "Nexus 7"
    WIDTH = "1920"
    HEIGHT = "1200"
    LOCATE = "H"

    EXERCISES_X = "1632"
    EXERCISES_Y = "439"
    EXERCISES_WIDTH = "190"
    EXERCISES_HEIGHT = "130"

    DOCKING_X = "720"
    DOCKING_Y = "270"
    DOCKING_WIDTH = "430"
    DOCKING_HEIGHT = "100"

if __name__ == "__main__":
    print(eval("_07daed71.%s" % "TMP_PICTURE"))
