# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy

from oucfeed import db


class Root(object):

    exposed = True

    def GET(self):
        return "OUC Feed"
