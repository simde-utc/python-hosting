#!/usr/env/python

import sys
import os
import sh

ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT_SITES_AVAILABLE = os.path.join(ROOT, 'sites-available')
ROOT_SITES_ENABLED = os.path.join(ROOT, 'sites-enabled')

def loc_site_available(site):
	return os.path.join(ROOT_SITES_AVAILABLE, site)
	
def loc_site_enabled(site):
	return os.path.join(ROOT_SITES_ENABLED, site)

def enable_site(site):
	av = loc_site_available(site)
	en = loc_site_enabled(site)
	if os.path.exists(en):
		print "%s is already enabled" % site
	elif not os.path.exists(av):
		print "%s does not exist" % site
	else:
		sh.ln('-s', av, en)
		print "Successfully enabled %s, restart nginx and supervisord" % site

def disable_site(site):
	en = loc_site_enabled(site)
	if not os.path.exists(en):
		print "%s is not enabled" % site
	else:
		sh.rm(en)
		print "Successfully disabled %s, restart nginx and supervisord" % site

