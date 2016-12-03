#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'KhaVu'
SITENAME = "Vũ Quang Khả's website"
HOMENAME = "Home"
SITEURL = 'http://vuquangkha.com'

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# KhaVu edit
STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

THEME = "/data/nginx-html/pelican-themes/pelican-bootstrap3"
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
FAVICON = 'my-bootstrap/favicon.png" type="image/png'


PLUGIN_PATHS = ["/data/nginx-html/pelican-plugins"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_MAX_ITEMS = 10

SOCIAL = (('facebook', 'https://www.facebook.com/kha.vuquang'),
	  ('linkedin', 'https://www.linkedin.com/in/khavu'),
	  ('skype', 'skype:vqk_yamaha?chat'),
	  ('email', 'mailto:vuquangkha@gmail.com'),
	  ('rss', 'http://vuquangkha.com/feeds/all.atom.xml'),)

DISQUS_SITENAME = 'vuquangkha-com'
DISQUS_NO_ID = False
DISQUS_DISPLAY_COUNTS = True
DISQUS_ID_PREFIX_SLUG = False

GOOGLE_ANALYTICS = 'UA-88421104-1'
DISPLAY_CATEGORIES_ON_MENU = True

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}.html'
CATEGORIES_SAVE_AS = 'categories.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = False
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags'
