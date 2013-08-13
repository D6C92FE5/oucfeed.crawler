# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import json
import hashlib

import cherrypy
from cherrypy import request, response

from oucfeed import db, util


class Profile(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, id_):
        return db.get_profile(id_)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        id_ = generate_profile_id(request.json)
        db.set_profile(id_, request.json)
        return {'id': id_}


generate_profile_id = util.json_sha1_base64


def match(profile, category):
    for part in category:
        profile = profile.get(part)
        if profile == {}:
            return True
        if not profile:
            break
    return bool(profile)
