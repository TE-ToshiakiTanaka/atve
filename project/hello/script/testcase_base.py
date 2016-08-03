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

    def arg_parse(self, parser):
        parser.add_argument(action='store', dest="testcase",
                            help='TestCase Name.')
        return parser

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
