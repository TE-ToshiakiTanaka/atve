import os
import sys
import time

from atve.log import Log
from atve.script import AtveTestCase


class TestCase(AtveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        print("*** Start TestCase   : %s *** " % __file__)

    def test(self):
        self.assertTrue(False)

    @classmethod
    def tearDownClass(cls):
        print("*** End TestCase     : %s *** " % __file__)
