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
        """
        #self.adb.build_uiautomator(AUBS_JAR_DIR)
        self.adb.push_uiautomator(os.path.join(AUBS_JAR_DIR, "bin", self.adb.get().JAR_AUBS))


    def get_reference(self, reference):
        try:
            return os.path.join(TMP_DIR, self.adb.get().SERIAL, reference)
        except Exception as e:
            L.warning(e); raise e

    def get_target(self, target):
        try:
            return os.path.join(TMP_DIR, target)
        except Exception as e:
            L.warning(e); raise e

    def enable_timeout(self, reference, target=None, loop=5, timeout=5):
        result = False
        for _ in range(loop):
            if self.enable(reference): result = True; break
            time.sleep(timeout)
        return result

    def enable(self, reference, target=None):
        L.debug("reference : %s" % reference)
        if target == None:
            self.adb_screenshot(self.adb.get().TMP_PICTURE)
            target = self.adb.get().TMP_PICTURE
        return self.picture_is_pattern(
            self.get_target(target), self.get_reference(reference))

    def tap_timeout(self, reference, target=None, loop=5, timeout=5):
        if not self.enable_timeout(reference, target, loop, timeout):
            return False
        return self.tap(reference)

    def tap(self, reference, target=None):
        L.debug("reference : %s " % reference)
        if target == None:
            self.adb_screenshot(self.adb.get().TMP_PICTURE)
            target = self.adb.get().TMP_PICTURE
        result = self.picture_find_pattern(
            self.get_target(target), self.get_reference(reference))
        if not result == None:
            L.info(self._tap(result))
            return True
        else:
            return False

    def _tap(self, result):
        x = int(result.y) + int(result.height / 2)
        y = int(self.adb.get().WIDTH) - (int(result.x) + int(result.width / 2))
        return self.adb_tap(x, y)
