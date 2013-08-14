# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


import os


SQLITE_PATH = None

GAE = "APPLICATION_ID" in os.environ

EXPORT_COUNT_DEFAULT = 10
EXPORT_COUNT_MIN = 1
EXPORT_COUNT_MAX = 50
