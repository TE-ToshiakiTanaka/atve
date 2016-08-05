import os
import sys
import argparse
try:
    import configparser
except:
    import ConfigParser as configparser

from atve.script import AtveTestCase
from fleet.utility import *
from fleet.utility import LOG as L

class TestCase_Unit(AtveTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase_Unit, self).__init__(*args, **kwargs)
        self.get_config()
        self.get_service()

    def arg_parse(self, parser):
        parser.add_argument(action='store', dest="testcase",
                            help='TestCase Name.')
        parser.add_argument('-m', action='store', dest='mobile',
                            help='Mobile (Android) Serial ID.')
        parser.add_argument('-f', action='store', dest='fleet',
                            help='Fleet Number. (1 ~ 4)')
        parser.add_argument('-e', action='store', dest='expedition',
                            help='Expedition ID.')
        parser.add_argument('-j', action='store', dest='job',
                            help='Jenkins Job.')
        parser.add_argument('-t', action='store', dest='timeout',
                            help='Timeout.')
        parser.add_argument('-u', action='store', dest='url',
                            help='target Jenkins URL.')
        return parser

    @classmethod
    def get_service(cls):
         cls.adb = cls.service["atve.android"].get(cls.get("args.mobile"), PROFILE_DIR)
         # cls.browser = cls.service["atve.browser"].get()
         cls.picture = cls.service["atve.picture"].get()

    @classmethod
    def get_config(cls, conf=""):
        if conf == "":
            conf = os.path.join(SCRIPT_DIR, "config.ini")
        try:
            config = configparser.ConfigParser()
            config.read(conf)
            for section in config.sections():
                for option in config.options(section):
                    cls.set("%s.%s" % (section, option), config.get(section, option))
        except Exception as e:
            L.warning('error: could not read config file: %s' % e)
