# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from itertools import islice

import cherrypy
from cherrypy import request, response
from webhelpers import feedgenerator

from oucfeed import db, util, news


feed_generators = {
    'atom': feedgenerator.Atom1Feed,
    'rss': feedgenerator.Rss201rev2Feed,
}

class Feed(object):

    exposed = True

    generator = feedgenerator.DefaultFeed

    def __init__(self, feed_type='rss'):
        self.generator = feed_generators[feed_type]

    def GET(self, id_, count=None):
        count = util.parse_output_count(count)
        profile = db.get_profile(id_)

        feed = self.generator(
            title="OUC Feed",
            link=cherrypy.url(),
            description="中国海洋大学 订阅源",
            subtitle="中国海洋大学 订阅源",
            language="zh-CN",
        )
        for item in islice(news.filtered_by_profile(profile), count):
            feed.add_item(
                title="[{}]{}".format("/".join(item['category']), item['title']),
                link=item['link'],
                description=item['content'],
                pubdate=util.parse_datetime(item['datetime']),
                unique_id=item['id']
            )

        response.headers['Content-Type'] = self.generator.mime_type
        return feed.writeString('utf-8')
