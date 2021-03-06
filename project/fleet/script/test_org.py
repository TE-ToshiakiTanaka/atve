import os
import sys
import time

from atve.cmd import run_ab

from fleet.utility import *
from fleet.utility import LOG as L
from fleet.script import testcase_normal

class TestCase(testcase_normal.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test_1(self):
        L.info("*** Test 01 ***")
        # self.supply_and_docking(self.get("args.fleet"))
        # self.assertTrue(self.initialize())
        #while self.expedition_result(): time.sleep(3)
        # self.assertTrue(self.docking())
        # self.assertTrue(self.home())
        self.adb_screenshot("capture.png")
        #self.assertTrue(self.enable_pattern("attack_rack*"))
        #self.assertTrue(self.enable_pattern("attack_damage*"))
        #self.assertTrue(self.initialize())

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
