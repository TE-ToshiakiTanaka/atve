import os
import sys
import time

from fleet.script import testcase_android
from fleet.script import testcase_picture
from fleet.utility import *
from fleet.utility import LOG as L

class TestCase_Base(testcase_android.TestCase_Android,
                    testcase_picture.TestCase_Picture):

    def __init__(self, *args, **kwargs):
        super(TestCase_Base, self).__init__(*args, **kwargs)
        """
        self.adb.install_application(AURA_APK_DIR)
        self.adb.exec_application(self.adb.get().AURA_DEBUGON, {})

        self.adb.build_uiautomator(AUBS_JAR_DIR)
        self.adb.push_uiautomator(os.path.join(AUBS_JAR_DIR, "bin", self.adb.get().JAR_AUBS))
        """
