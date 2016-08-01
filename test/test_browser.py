import os
import platform
from nose.tools import with_setup, raises, ok_, eq_

from atve.log import LOG as L
from atve.script import AtveTestCase
from runner import TestAtveTestRunner as TSTR


class TestBrowserTestRuner(TSTR):
    def get_driver_path(self):
        if platform.system() == "Linux":
            return os.path.join(
                self.bin_path, "webdriver", "chrome",
                    platform.system(), platform.processor(), "chromedriver")
        elif platform.system() == "Windows":
            return os.path.join(
                self.bin_path, "webdriver", "chrome",
                    platform.system(), "chromedriver.exe")
        else:
            return None

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_01(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_01.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_02(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_02.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_03(self):
        self.script_path = os.path.join(self.script_path, "browser")
        self.base_library_execute_success("browser_03.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04(self):
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_3(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_driver_path()
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        AtveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_04_3.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_04_4(self):
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_04_4.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_05(self):
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_05.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_05_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_driver_path()
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        AtveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_05_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_06(self):
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_06.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_06_2(self):
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_driver_path()
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        AtveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_06_2.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_07(self):
        AtveTestCase.set("system.tmp", self.tmp_path)
        self.script_path = os.path.join(self.script_path, "browser")
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        self.base_library_execute_success("browser_07.py")

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_browser_success_07_2(self):
        AtveTestCase.set("system.tmp", self.tmp_path)
        self.script_path = os.path.join(self.script_path, "browser")
        driver_path = self.get_driver_path()
        AtveTestCase.set("browser.url", u'https://www.google.com/')
        AtveTestCase.set("browser.driver", driver_path)
        self.base_library_execute_success("browser_07_2.py")
