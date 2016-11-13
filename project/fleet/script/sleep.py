import os
import sys
import json
import urllib2
import base64
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
            username = self.get("args.userid")
            token = self.get("args.password")

            url = "%s/job/%s/api/json?token=%s" % (self.get("args.url"), self.get("args.job"), self.get("args.job"))
            L.info(url)
            request = urllib2.Request(url)
            base64string = base64.encodestring('%s:%s' % (username, token)).replace('\n', '')
            request.add_header("Authorization", "Basic %s" % base64string)

            r = urllib2.urlopen(request)
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
            url2 = "%s/job/%s/build?token=%s&delay=0sec" % (self.get("args.url"), self.get("args.job"), self.get("args.job"))
            L.info(url2)

            request2 = urllib2.Request(url2)
            base64string2 = base64.encodestring('%s:%s' % (username, token)).replace('\n', '')
            request2.add_header("Authorization", "Basic %s" % base64string2)

            r2 = urllib2.urlopen(request2)
            L.debug("HTTP Status Code : %d" % r2.getcode())
            self.assertTrue(r2.getcode() == 201)
        finally:
            r2.close()

    @classmethod
    def tearDownClass(cls):
        L.info("*** End TestCase   : %s *** " % __file__)
