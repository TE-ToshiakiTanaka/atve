import os
import sys

from android_base import Android

class _07daed71(Android):
    SERIAL = "07daed71"
    TMP_PICTURE="%s_TMP.png" % SERIAL
    IP = ""
    PORT = ""

    NAME = "Nexus 7"
    WIDTH = "1080"
    HEIGHT = "1920"
    LOCATE = "H"

if __name__ == "__main__":
    print(eval("_07daed71.%s" % "TMP_PICTURE"))
