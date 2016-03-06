#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Angus Griffith'
SITENAME = 'blog.angusgriffith.com'
SITEURL = 'https://blog.angusgriffith.com'

TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False
PDF_GENERATOR = False

SOCIAL = (('twitter', 'http://twitter.com/sn6uv'),
          ('github', 'http://github.com/sn6uv'))

OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

STATIC_PATHS = ["images"]

THEME = 'notmyidea'

PLUGINS = ["latex"]

GOOGLE_ANALYTICS = 'UA-64441388-1'

# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
