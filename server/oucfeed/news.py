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
        history = set(db.get_news_history())

        news_new = {x['id']: x for x in request.json if x['id'] not in history}
        news.extend(news_new.itervalues())
        history.update(news_new.iterkeys())

        db.set_news(news[-1000:])
        db.set_news_history(list(history))

        return ""
