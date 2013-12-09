#!/usr/bin/env python

import sys
import os
import sh

from scripts.utils import *

def create_site(site):
    ss = loc_site(site)
    gid = 'web'
    print "Create site dir for %s..." % site,
    if os.path.exists(ss):
        print 'Already existing'
    else:
        sh.cp('-a', SITE_TEMPLATE_PATH, ss)
        print "OK"
    print 'chown %s:%s %s ...' % (site, gid, ss),
    sh.chown('-R', '%s:%s' % (site, gid), ss)
    print 'Ok'
    print 'chmod 2750 %s ...' % ss,
    sh.chmod('2750', ss)
    print 'Ok'
    

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



