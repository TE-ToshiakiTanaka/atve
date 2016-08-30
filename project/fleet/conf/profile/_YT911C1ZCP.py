import os
import sys

from android_base import Android

class _YT911C1ZCP(Android):
    SERIAL = "YT911C1ZCP"
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

    FORMATION_X = "395"
    FORMATION_Y = "210"
    FORMATION_WIDTH = "75"
    FORMATION_HEIGHT = "305"

if __name__ == "__main__":
    print(eval("_YT911C1ZCP.%s" % "TMP_PICTURE"))
