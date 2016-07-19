import os
import sys

class Factory(object):
    def __init__(self):
        pass

    def get(self):
        return True


NAME = "core"
FACTORY = Factory()
