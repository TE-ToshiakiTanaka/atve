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
        result = False
        try:
            url = "%s/job/%s/api/json" % (self.get("jenkins.url"), self.get("args.job"))
            L.info(url)
            r = urllib2.urlopen(url)
            root = json.loads(r.read())
            latest = int(root['lastBuild']['number'])
            success = int(root['lastStableBuild']['number'])
            L.debug("Latest Number  : %d" % latest )
            L.debug("Success Number : %d" % success )
            result = latest == success
        finally:
            r.close()
        if result:
            timeout = int(self.get("args.timeout"))
            L.debug("Timeout : %d " % timeout)
            time.sleep(timeout)
        else:
            L.debug("Retry.")
        try:
            url2 = "%s/job/%s/build?delay=0sec" % (self.get("jenkins.url"), self.get("args.job"))
            r2 = urllib2.urlopen(url2)
            L.debug("HTTP Status Code : %d" % r2.getcode())
            self.assertTrue(r2.getcode() == 201)
        finally:
            r2.close()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase   : %s *** " % __file__)
