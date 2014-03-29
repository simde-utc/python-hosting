#!/usr/bin/env python

import sys
import os

DIR = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(DIR, '..'))
ROOT_TEMPLATES = os.path.join(ROOT, 'templates')
TMPL_PATH = os.path.join(ROOT_TEMPLATES, 'logrotate.conf')
ROOT_CONF = os.path.join(ROOT, 'conf')
SITES_PATH_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')
DEST_PATH = os.path.join(ROOT, 'logrotate.conf')


def make_conf():
    sites_path = open(SITES_PATH_PATH).read()
    tmpl = open(TMPL_PATH).read()
    r = tmpl.replace('<%root%>', sites_path)
    print r
    open(DEST_PATH, 'w').write(r)

if __name__ == '__main__':
    make_conf()
