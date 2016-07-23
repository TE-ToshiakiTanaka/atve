import os
import sys
import time

from atve.log import LOG as L
from atve.exception import *
from atve.script import AtveTestCase


class TestCase(AtveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        L.info("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        try :
            self.assertTrue("atve.browser" in self.service.keys())
            b = self.service["atve.browser"].get("Chrome")
            self.assertTrue(b != None)
            b.start(self.get("browser.url"))
            self.assertTrue(False)
        except SeleniumError as e:
            L.warning(str(e))
        except Exception as e:
            self.assertTrue(False)

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase     : %s *** " % __file__)
