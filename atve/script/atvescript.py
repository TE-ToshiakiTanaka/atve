import os
import sys
import time
import argparse
import unittest
import importlib

from atve.log import LOG as L
from atve.exception import *

SYSTEM_LIBRARY = os.path.normpath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "library"))


class AtveTestCase(unittest.TestCase):
    config = {}
    service = {}

    def __init__(self, *args, **kwargs):
        global service
        super(AtveTestCase, self).__init__(*args, **kwargs)
        self.register(SYSTEM_LIBRARY)
        self.__parse()

    @classmethod
    def register(cls, host):
        if not os.path.exists(host):
            raise LibraryError("%s is not exists." % (host))
        for fdn in os.listdir(host):
            try:
                if fdn.endswith(".pyc") or fdn.endswith(".py"):
                    pass
                else:
                    sys.path.append(os.path.join(host, fdn))
                    module = importlib.import_module("service")
                    cls.service[module.NAME] = module.FACTORY
                    sys.path.remove(os.path.join(host, fdn))
            except Exception as e:
                sys.path.remove(os.path.join(host, fdn))
                L.warning(type(e).__name__ + ": " + str(e))


    @classmethod
    def set(cls, name, value):
        cls.config[name] = value

    @classmethod
    def get(cls, name):
        return cls.config[name]

    def __parse(self):
        parser = argparse.ArgumentParser()

        parser = self.arg_parse(parser)

        results = parser.parse_args()
        for k, v in vars(results).items():
            self.set("args.%s" % k, v)

    def arg_parse(self, parser):
        parser.add_argument(action='store', dest="testcase",
                            help='TestCase Name.')
        return parser


    @classmethod
    def get_service(cls, settings):
        pass
