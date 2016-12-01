#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'KhaVu'
SITENAME = "Vũ Quang Khả's website"
HOMENAME = "Home"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# KhaVu edit
STATIC_PATHS = ['images']
THEME = "/data/nginx-html/my-website/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'superhero'
PYGMENTS_STYLE = 'native'
BOOTSTRAP_FLUID = False
BOOTSTRAP_NAVBAR_INVERSE = True
USE_PAGER = True
BANNER = 'images/cover.jpg'
HIDE_SITENAME = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
