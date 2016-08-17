import os
import sys

from android_base import Android

class _YT9111NUXX(Android):
    SERIAL = "YT9111NUXX"
    TMP_PICTURE="%s_TMP.png" % SERIAL
    IP = ""
    PORT = ""

    NAME = "Xperia Z3C"
    WIDTH = "720"
    HEIGHT = "1280"
    LOCATE = "V"

    EXERCISES_X = "380"
    EXERCISES_Y = "1060"
    EXERCISES_WIDTH = "81"
    EXERCISES_HEIGHT = "100"

    DOCKING_X = "500"
    DOCKING_Y = "490"
    DOCKING_WIDTH = "67"
    DOCKING_HEIGHT = "750"

if __name__ == "__main__":
    print(eval("_YT9111NUXX.%s" % "TMP_PICTURE"))
