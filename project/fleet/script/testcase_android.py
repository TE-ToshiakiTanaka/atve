import os
import sys

from fleet.utility import *
from fleet.utility import LOG as L
from fleet.script import testcase_base


class TestCase_Android(testcase_base.TestCase_Unit):

    def adb_screenshot(self, filename=None):
        if filename == None: filename = "capture.png"
        return self.adb.snapshot(filename, TMP_DIR)

    def adb_tap(self, x, y):
        return self.adb.tap(x, y)
