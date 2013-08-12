# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

import db


class News(object):

    exposed = True

    @cherrypy.tools.json_in()
    def POST(self):
        news = db.get_news()
        news.append(request.json)
        db.set_news(news[-1000:])
        return ""
