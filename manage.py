#!/usr/bin/env python

import sys
import os
import sh

ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT_CONF = os.path.join(ROOT, 'conf')
SITES_PATH_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')
ROOT_UWSGI = os.path.join(ROOT, 'uwsgi')
ROOT_TEMPLATES = os.path.join(ROOT, 'templates')
ROOT_UWSGI_CONF = os.path.join(ROOT_UWSGI, 'conf')
UWSGI_CONF_VASSAL = os.path.join(ROOT_UWSGI_CONF, 'vassal.ini')
ROOT_UWSGI_VASSALS = os.path.join(ROOT_UWSGI, 'vassals')
SITE_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATES, 'site')

def loc_site(site):
    sites_path = open(SITES_PATH_PATH).read()
    return os.path.join(sites_path, site)

def loc_uwsgi_conf(site):
    return os.path.join(ROOT_UWSGI_VASSALS, site+'.ini')

def create_site(site):
    ss = loc_site(site)
    print "Create site dir for %s..." % site,
    if os.path.exists(ss):
        print 'Already existing'
        sh.chown('-R', site+':web', ss)
    else:
        sh.cp('-a', SITE_TEMPLATE_PATH, ss)
        sh.chown('-R', site+':web', ss)
        print "OK"

def enable_site(site):
    uc = loc_uwsgi_conf(site)
    ss = loc_site(site)
    if not os.path.exists(ss):
        print "%s does not exist" % site
    elif os.path.exists(uc):
        print "%s is already enabled" % site
    else:
        sh.ln('-s', UWSGI_CONF_VASSAL, uc)
        print "Successfully enabled %s" % site

def disable_site(site):
    uc = loc_uwsgi_conf(site)
    if not os.path.exists(uc):
        print "%s is not enabled" % site
    else:
        sh.rm(uc)
        print "Successfully disabled %s" % site




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: ./manage.py <site> <command>"
        exit(1)
    if sh.whoami().strip() != 'root':
        print sh.whoami().strip(), "you must be root !"
        exit(1)
    site,cmd = sys.argv[1::]
    func = locals()[cmd+'_site']
    func(site)



