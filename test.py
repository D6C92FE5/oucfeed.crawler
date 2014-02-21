#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os

from oucfeed.crawler.executor import run


if os.path.exists("test.js"):
    os.remove("test.js")
run(["党委研究生工作部"])
