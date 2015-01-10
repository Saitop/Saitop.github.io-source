#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hansun Lam'
SITENAME = 'Hansun Lam'
SITEURL = 'http://saitop.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_DATE = 'fs'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS= [('Home', SITEURL)]
#THEME = "pelican-themes/subtle"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('Github','https://github.com/Saitop'),
          ('Facebook','https://www.facebook.com/profile.php?id=100004344064855'),
          ('google-plus','https://plus.google.com/u/0/117007028957634159499/posts/p/pub'),
          #('You can add links in your config file', '#'),
          #('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILES_TO_COPY=(
               ('extra/CNAME','CNAME'),
               )


