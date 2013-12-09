
import sys
import os

ROOT_SCRIPTS = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(ROOT_SCRIPTS, '..'))
ROOT_CONF = os.path.join(ROOT, 'conf')
ROOT_UWSGI = os.path.join(ROOT, 'uwsgi')
ROOT_TEMPLATES = os.path.join(ROOT, 'templates')
ROOT_UWSGI_CONF = os.path.join(ROOT_UWSGI, 'conf')
ROOT_UWSGI_VASSALS = os.path.join(ROOT_UWSGI, 'vassals')

PATH_SITE_TEMPLATE = os.path.join(ROOT_TEMPLATES, 'site')
PATH_VASSAL_TEMPLATE = os.path.join(ROOT_TEMPLATES, 'vassal.ini')
PATH_SITES_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')
PATH_VASSAL_CONF = os.path.join(ROOT_UWSGI_CONF, 'vassal.ini')


def loc_site(site):
    sites_path = open(PATH_SITES_PATH).read()
    return os.path.join(sites_path, site)

def loc_uwsgi_conf(site):
    return os.path.join(ROOT_UWSGI_VASSALS, site+'.ini')


def _ask_root_sites():
    def ask_sites_path():
        return os.path.abspath(raw_input('Absolute path to site directory: '))
    sites_path = ask_sites_path()
    while not os.path.exists(sites_path):
        print '%s is not a valid path' % sites_path
        sites_path = ask_sites_path()
    return sites_path

if os.path.exists(PATH_SITES_PATH):
    ROOT_SITES = open(PATH_SITES_PATH).read()
else:
    print 'Your hosting has not been configured yet'
    ROOT_SITES = _ask_root_sites()
    open(PATH_SITES_PATH, 'w').write(ROOT_SITES)
