import sys
import os

# scripts directory
ROOT_SCRIPTS = os.path.abspath(os.path.dirname(__file__))
# project root directory
ROOT = os.path.abspath(os.path.join(ROOT_SCRIPTS, '..'))
# project config directory
ROOT_CONF = os.path.join(ROOT, 'conf')
# uwsgi directory
ROOT_UWSGI = os.path.join(ROOT, 'uwsgi')
# template directory
ROOT_TEMPLATES = os.path.join(ROOT, 'templates')
# uwsgi conf directory
ROOT_UWSGI_CONF = os.path.join(ROOT_UWSGI, 'conf')
# vassals directory
ROOT_UWSGI_VASSALS = os.path.join(ROOT_UWSGI, 'vassals')

# path to the site template
PATH_SITE_TEMPLATE = os.path.join(ROOT_TEMPLATES, 'site')
# path to the vassal template
PATH_VASSAL_TEMPLATE = os.path.join(ROOT_TEMPLATES, 'vassal.ini')
# path to the config for sites root 
PATH_SITES_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')
# path to the default vassal config
PATH_VASSAL_CONF = os.path.join(ROOT_UWSGI_CONF, 'vassal.ini')

# web group id
WEB_GID = 'web'

def loc_site(site):
    ''' get the path to the root directory of a site '''
    sites_path = open(PATH_SITES_PATH).read()
    return os.path.join(sites_path, site)

def loc_uwsgi_conf(site):
    ''' get the path to the uwsgi config of a site '''
    return os.path.join(ROOT_UWSGI_VASSALS, site+'.ini')

def loc_app_dir(site):
    return os.path.join(loc_site(site), 'app')

def loc_static_dir(site):
    return os.path.join(loc_site(site), 'static')

def loc_wsgi_dir(site):
    return os.path.join(loc_app_dir(site), 'wsgi')
    

def _ask_root_sites():
    def ask_sites_path():
        return os.path.abspath(raw_input('Absolute path to site directory: '))
    sites_path = ask_sites_path()
    while not os.path.exists(sites_path):
        print '%s is not a valid path' % sites_path
        sites_path = ask_sites_path()
    return sites_path

# compute the rott directory of sites
if os.path.exists(PATH_SITES_PATH):
    ROOT_SITES = open(PATH_SITES_PATH).read()
else:
    print 'Your hosting has not been configured yet'
    ROOT_SITES = _ask_root_sites()
    open(PATH_SITES_PATH, 'w').write(ROOT_SITES)
