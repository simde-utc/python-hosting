#!/usr/bin/env python

import sys
import os
import sh

ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT_DATA = os.path.join(ROOT, 'data')
ROOT_SITES = os.path.join(ROOT, 'sites')
ROOT_UWSGI = os.path.join(ROOT, 'uwsgi')
ROOT_UWSGI_CONF = os.path.join(ROOT_UWSGI, 'conf')
UWSGI_CONF_VASSAL = os.path.join(ROOT_UWSGI_CONF, 'vassal.ini')
ROOT_UWSGI_VASSALS = os.path.join(ROOT_UWSGI, 'vassals')

def loc_site_data(site):
    return os.path.join(ROOT_DATA, site)

def loc_site_site(site):
    return os.path.join(ROOT_SITES, site)

def loc_uwsgi_conf(site):
    return os.path.join(ROOT_UWSGI_VASSALS, site+'.ini')

def create_site(site):
    sd = loc_site_data(site)
    ss = loc_site_site(site)
    
    print "Create data dir for %s..." % site,
    if os.path.exists(sd):
        print 'Already existing'
    else:
        sh.cp('-an', loc_site_data('sample'), sd)
        sh.chown('-R', site+':'+site, sd)
        print "OK"
    
    print "Create site dir for %s..." % site,
    if os.path.exists(ss):
        print 'Already existing'
    else:
        sh.cp('-an', loc_site_site('sample'), ss)
        sh.chown('-R', site+':'+site, ss)
        print "OK"

def enable_site(site):
    uc = loc_uwsgi_conf(site)
    sd = loc_site_data(site)
    ss = loc_site_site(site)
    if not os.path.exists(sd) or not os.path.exists(ss):
        print "%s does not exist" % site
    elif os.path.exists(uc):
        print "%s is already enabled" % site
    else:
        sh.ln('-s', UWSGI_CONF_VASSAL, uc)
        print "Successfully enabled %s, restart supervisord" % site

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
        print sh.whoami()
        print "You must be root !"
        exit(1)
    site,cmd = sys.argv[1::]
    func = locals()[cmd+'_site']
    func(site)



