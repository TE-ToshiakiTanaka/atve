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
        self.assertTrue("atve.browser" in self.service.keys())
        b = self.service["atve.browser"].get("FireFox")
        self.assertTrue(b != None)
        b.start(self.get("browser.url"))
        self.assertTrue(b.find_element_by_id("hplogo") != None)
        b.quit()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
