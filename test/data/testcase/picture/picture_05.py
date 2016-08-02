import os
import sys
import time

from atve.log import LOG as L
from atve.script import AtveTestCase


class TestCase(AtveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        self.assertTrue("atve.picture" in self.service.keys())
        self.assertTrue(self.service["atve.picture"].version() != None)
        pic = self.service["atve.picture"].get()

        self.assertTrue(self.get("system.tmp") != None)
        L.info(os.path.join(self.get("system.tmp"), "test01.png"))
        pic.info(pic.open(os.path.join(self.get("system.tmp"), "test01.png")))

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
