# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


try:
    from google.appengine.ext import ndb
except:
    from oucfeed.db.sqlite import *
else:
    from oucfeed.db.gae import *
