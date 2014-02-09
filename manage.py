#!/usr/bin/env python

import sys
import os
import sh
import pwd

from scripts.utils import *

def create_site(site):
    '''
    Create the site directory from the template
    1. copy the template
    2. change permissions
    
    /               rwxr-xr-x   site:site_grp
    |-- app         rwx------   site:site_grp
    `-- static      rwxr-s---   site:web
    
    '''
    ss = loc_site(site)
    gid = pwd.getpwnam(site).pw_gid
    print "Create site dir for %s..." % site,
    if os.path.exists(ss):
        print 'Already existing'
    else:
        sh.cp('-a', PATH_SITE_TEMPLATE, ss)
        print "OK"
    # process root
    print 'chown %s:%s %s ...' % (site, gid, ss),
    sh.chown('-R', '%s:%s' % (site, gid), ss)
    print 'Ok'
    print 'chmod 755 %s ...' % ss,
    sh.chmod('755', ss)
    print 'Ok'
    # process app dir
    app_dir = loc_app_dir(site)
    print 'chmod 700 %s ...' % app_dir,
    sh.chmod('700', app_dir)
    print 'Ok'
    # process static dir
    static_dir = loc_static_dir(site)
    print 'chown %s:%s %s ...' % (site, WEB_GID, static_dir),
    sh.chown('-R', '%s:%s' % (site, WEB_GID), static_dir)
    print 'Ok'
    print 'chmod 2750 %s ...' % static_dir,
    sh.chmod('2750', static_dir)
    print 'Ok'


def enable_site(site):
    uc = loc_uwsgi_conf(site)
    ss = loc_site(site)
    if not os.path.exists(ss):
        print "%s does not exist" % site
    elif os.path.exists(uc):
        print "%s is already enabled" % site
    else:
        sh.ln('-s', PATH_VASSAL_CONF, uc)
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



