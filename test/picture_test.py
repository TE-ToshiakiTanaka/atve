import os
from atve.script import AtveTestCase
from runner import TestAtveTestRunner as TSTR
from nose.tools import with_setup, raises, ok_, eq_

class TestPictureTestRuner(TSTR):

    @with_setup(TSTR.setup, TSTR.teardown)
    def test_library_execute_picture_success_01(self):
        self.script_path = os.path.join(self.script_path, "picture")
        self.base_library_execute_success("picture_01.py")
