import os
import sys

from android_base import Android

class _YT9111NUXX(Android):
    SERIAL = "YT9111NUXX"
    TMP_PICTURE="%s_TMP.png" % SERIAL
    IP = ""
    PORT = ""

if __name__ == "__main__":
    print(eval("_YT9111NUXX.%s" % "TMP_PICTURE"))
