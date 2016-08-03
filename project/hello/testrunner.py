import os
import sys
import atve

PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if not PATH in sys.path:
    sys.path.insert(0, PATH)

if atve.__version__ < "0.1.0":
    sys.exit("stve version over 0.1.0. : %s " % (atve.__version__))

from atve.application import AtveTestRunner
from atve.workspace import Workspace

from hello.utility import *
from hello.script.testcase_base import TestCase_Unit

class TestRunner(object):
    def __init__(self):
        self.runner = AtveTestRunner()
        self.workspace = Workspace(WORK_DIR)

        self.tmp = self.workspace.mkdir("tmp")
        self.log = self.workspace.mkdir("log")
        self.report = self.workspace.mkdir("report")

        #TestCase_Unit.register(LIB_DIR)

    def execute(self, script):
        self.runner.execute(script, SCRIPT_DIR)

    def execute_with_report(self, script):
        self.runner.execute_with_report(script, SCRIPT_DIR, self.report)

if __name__ == "__main__":
    if len(sys.argv[1:]) < 1:
        sys.exit("Usage: %s <filename>" % sys.argv[0])
    testcase = sys.argv[1]
    runner = TestRunner()
    runner.execute_with_report(testcase)
