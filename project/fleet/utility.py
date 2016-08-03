import os
import sys
import logging

from atve import log

WORK_DIR = os.path.normpath(os.path.dirname(__file__))
LIB_DIR = os.path.normpath(os.path.join(WORK_DIR, "lib"))
SCRIPT_DIR = os.path.normpath(os.path.join(WORK_DIR, "script"))
TMP_DIR = os.path.normpath(os.path.join(WORK_DIR, "tmp"))
LOG_DIR = os.path.normpath(os.path.join(WORK_DIR, "log"))
BIN_DIR = os.path.normpath(os.path.join(WORK_DIR, "bin"))

PROFILE_DIR = os.path.normpath(os.path.join(WORK_DIR, "conf", "profile"))

AURA_APK_DIR = os.path.normpath(os.path.join(BIN_DIR, "apk", "aura"))
AUBS_JAR_DIR = os.path.normpath(os.path.join(BIN_DIR, "jar", "aubs"))

LOG = log.Log("Project.ATVE")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
logfile = os.path.join(LOG_DIR, "system.log")
if not os.path.exists(logfile):
    with open(logfile, 'a') as f:
        os.utime(logfile, None)

LOG.addHandler(log.Log.fileHandler(logfile, log.BASE_FORMAT, logging.DEBUG))
