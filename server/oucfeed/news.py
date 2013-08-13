# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

from oucfeed import db, category


class News(object):

    exposed = True

    @cherrypy.tools.json_in()
    def POST(self):
        add(request.json)
        return ""


def add(news_iter):
    history = db.get_news_history()

    news_new = {x['id']: x for x in news_iter if x['id'] not in history}
    for news in news_new.itervalues():
        news['category'] = tuple(news['category'].split("/"))

    history.update(news_new.iterkeys())
    db.set_news_history(history)

    news = db.get_news()
    news.extend(news_new.itervalues())
    db.set_news(news[-1000:])

    category.add(x['category'] for x in news_new.itervalues())
