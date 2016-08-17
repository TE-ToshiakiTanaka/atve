import os
import sys
import json
import urllib2
import time

from fleet.utility import *
from fleet.utility import LOG as L
from fleet.script import testcase_normal

class TestCase(testcase_normal.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test_step_1(self):
        timeout = int(self.get("args.timeout"))
        L.debug("Timeout : %d " % timeout * 3600)
        self.adb.stop("com.dmm.dmmlabo.kancolle/.AppEntry")
        time.sleep(timeout * 3600)

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase   : %s *** " % __file__)
