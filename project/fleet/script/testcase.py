import os
import sys
import time
import fnmatch
import random

from atve.exception import *

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

    def sleep(self, base=1):
        sleep_time = (0.5 + base * random.random())
        L.debug("sleep time : %s" % sleep_time)
        time.sleep(sleep_time)

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

    def enable_pattern_crop(self, pattern, point, filename=None, loop=3, timeout=0.5):
        references = self.__search_pattern(pattern)
        for ref in references:
            if self.enable_timeout_crop(
                ref, point, filename, loop=loop, timeout=timeout):
                return True
        return False

    def enable_pattern(self, pattern, target=None, loop=3, timeout=0.5):
        if target == None:
            target = self.adb_screenshot(self.adb.get().TMP_PICTURE)
        references = self.__search_pattern(pattern)
        for reference in references:
            if self.enable_timeout(reference, target, loop=loop, timeout=timeout):
                return True
        return False

    def tap_pattern(self, pattern, loop=3, timeout=0.5):
        targets = self.__search_pattern(pattern)
        for target in targets:
            if self.tap_timeout(target, loop=loop, timeout=timeout):
                return True
        return False

    def __search_pattern(self, pattern, host=""):
        result = []
        if host == "":
            host = os.path.join(TMP_DIR, self.adb.get().SERIAL)
        files = os.listdir(host)
        return fnmatch.filter(files, pattern)

    def enable_timeout_crop(self, reference, point, filename=None, loop=5, timeout=5):
        if filename == None:
            filename = self.adb_screenshot(self.adb.get().TMP_PICTURE)
        target = self.picture_crop(filename, point,
            self.get_target("crop_%s" % self.adb.get().TMP_PICTURE))
        L.info(target)
        return self.enable_timeout(reference, target, loop, timeout)

    def enable_timeout(self, reference, target=None, loop=5, timeout=5):
        result = False
        for _ in range(loop):
            if self.enable(reference, target): result = True; break
            time.sleep(timeout)
        return result

    def enable(self, reference, target=None):
        L.debug("reference : %s" % reference)
        if target == None:
            self.adb_screenshot(self.adb.get().TMP_PICTURE)
            target = self.adb.get().TMP_PICTURE
        return self.picture_is_pattern(
            self.get_target(target), self.get_reference(reference))

    def find(self, reference, target=None):
        L.debug("reference : %s " % reference)
        if target == None:
            self.adb_screenshot(self.adb.get().TMP_PICTURE)
            target = self.adb.get().TMP_PICTURE
        result = self.picture_find_pattern(
            self.get_target(target), self.get_reference(reference))
        if not result == None: return result
        else: return None

    def tap_timeout(self, reference, target=None, loop=5, timeout=5, threshold=0.2):
        if not self.enable_timeout(reference, target, loop, timeout):
            return False
        target = self.adb.get().TMP_PICTURE
        return self.tap(reference, target, threshold)

    def tap_timeout_crop(self, reference, point, filename=None, loop=5, timeout=5):
        if filename == None:
            filename = self.adb_screenshot(self.adb.get().TMP_PICTURE)
        target = self.picture_crop(filename, point,
            self.get_target("crop_%s" % self.adb.get().TMP_PICTURE))
        return self.tap_crop_inside(reference, target, point)

    def tap_crop_inside(self, reference, target, point):
        if target == None:
            return False
        result = self.picture_find_pattern(
            self.get_target(target), self.get_reference(reference))
        if not result == None:
            result.x = int(result.x) + int(point.x)
            result.y = int(result.y) + int(point.y)
            L.info("Target Point : %s" % result)
            L.info(self._tap(result))
            return True
        else:
            return False

    def tap(self, reference, target=None, threshold=0.2):
        if target == None:
            self.adb_screenshot(self.adb.get().TMP_PICTURE)
            target = self.adb.get().TMP_PICTURE
        result = self.picture_find_pattern(
            self.get_target(target), self.get_reference(reference))
        if not result == None:
            L.info(self._tap(result, threshold))
            return True
        else:
            return False

    def _tap(self, result, threshold=0.2):
        if self.adb.get().LOCATE == "H":
            x = int(result.x) + random.randint(int(int(result.width) * threshold) , int(int(result.width) * (1.0 - threshold)))
            y = int(result.y) + random.randint(int(int(result.height) * threshold) , int(int(result.height) * (1.0 - threshold)))
        else:
            x = int(result.y) + random.randint(int(int(result.height) * threshold) , int(int(result.height) * (1.0 - threshold)))
            y = int(self.adb.get().WIDTH) - (int(result.x) + random.randint(int(int(result.width) * threshold) , int(int(result.width) * (1.0 - threshold))))
        return self.adb_tap(x, y)

    def message(self, message):
        try:
            self.slack.message(message, self.get("args.channel"))
        except SlackError as e:
            L.warning(str(e))

    def upload(self, filepath):
        try:
            self.slack.upload(filepath, self.get("args.channel"))
        except SlackError as e:
            L.warning(str(e))
