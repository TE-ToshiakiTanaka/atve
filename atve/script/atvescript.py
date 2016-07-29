import os
import sys
import time
import argparse
import unittest
import importlib
import traceback

from atve.log import LOG as L
from atve.define import *
from atve.exception import *


class AtveTestCase(unittest.TestCase):
    config = {}
    service = {}

    def __init__(self, *args, **kwargs):
        global service
        super(AtveTestCase, self).__init__(*args, **kwargs)
        self.register(ATVE_LIB)
        self.__parse()

    @classmethod
    def register(cls, host):
        sys.path.append(host)
        if not os.path.exists(host):
            raise LibraryError("%s is not exists." % (host))
        for fdn in os.listdir(host):
            try:
                if fdn.endswith(".pyc") or fdn.endswith(".py"):
                    pass
                elif fdn.endswith("__pycache__"):
                    pass
                else:
                    package_path = os.path.join(host, fdn).split("\\")[len(ATVE_ROOT.split("\\")) - 1:]
                    package = ".".join(package_path)
                    module = importlib.import_module(".service", package)
                    cls.service[module.NAME] = module.FACTORY
            except Exception as e:
                L.warning(traceback.print_exc())
                L.warning(type(e).__name__ + ": " + str(e))
        print(cls.service)


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
