import os
from atve.script import AtveTestCase
from runner import TestAtveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestAndroidTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_01(self):
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_02(self):
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_03(self):
        AtveTestCase.set("android.serial", "emulator-5554")
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_android_success_04(self):
        AtveTestCase.set("android.serial", "emulator-5554")
        self.script_path = os.path.join(self.script_path, "android")
        self.base_library_execute_success("android_04.py")
