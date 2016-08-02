import os
import sys
import time

from fleet.script import testcase_base
from fleet.utility import *
from fleet.utility import LOG as L

class TestCase_Base(testcase_base.TestCase_Unit):

    def __init__(self, *args, **kwargs):
        super(TestCase_Base, self).__init__(*args, **kwargs)
