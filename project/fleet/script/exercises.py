import os
import sys
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

    def test_exercises(self):
        L.info("*** Exercises ***")
        self.assertTrue(self.initialize())
        while self.expedition_result(): time.sleep(3)
        self.message(self.get("bot.exercises"))
        self.assertTrue(self.exercises())
        while self.expedition_result(): time.sleep(3)
        self.assertTrue(self.supply(self.get("args.fleet")))
        self.assertTrue(self.home())


    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
