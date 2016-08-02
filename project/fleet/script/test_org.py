import os
import sys
import time

from fleet.utility import *
from fleet.utility import LOG as L
from fleet.script import testcase

class TestCase(testcase.TestCase_Base):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test_1(self):
        L.info("*** Test 01 ***")
        self.assertTrue(1 == 1)

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
