import os
from atve.script import AtveTestCase
from runner import TestAtveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestBrowserTestRuner(TSTR):

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
