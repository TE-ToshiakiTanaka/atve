import os
import sys
import logging

from atve import log

WORK_DIR = os.path.normpath(os.path.dirname(__file__))
SCRIPT_DIR = os.path.normpath(os.path.join(WORK_DIR, "script"))
TMP_DIR = os.path.normpath(os.path.join(WORK_DIR, "tmp"))
LOG_DIR = os.path.normpath(os.path.join(WORK_DIR, "log"))

LOG = log.Log("Project.ATVE")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
logfile = os.path.join(LOG_DIR, "system.log")
if not os.path.exists(logfile):
    with open(logfile, 'a') as f:
        os.utime(logfile, None)

LOG.addHandler(log.Log.fileHandler(logfile, log.BASE_FORMAT, logging.DEBUG))
