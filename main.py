#!/usr/bin/env python
import os
import jinja2
import webapp2

from handlers.base import BaseHandler, MainHandler, CookieAlertHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
], debug=True)
