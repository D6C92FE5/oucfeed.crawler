# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

import db


class Atom(object):

    exposed = True

