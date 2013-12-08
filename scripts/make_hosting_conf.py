#!/usr/bin/env python


import sys
import os



def get_sites_path():
    def ask_sites_path():
        return os.path.abspath(raw_input('Absolute path to site directory: '))
    sites_path = ask_sites_path()
    while not os.path.exists(sites_path):
        print '%s is not a valid path' % sites_path
        sites_path = ask_sites_path()
    return sites_path


if __name__ == '__main__':
    DIR = os.path.dirname(__file__)
    ROOT = os.path.abspath(os.path.join(DIR, '..'))
    ROOT_CONF = os.path.join(ROOT, 'conf')
    SITES_PATH_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')
    
    sites_path = get_sites_path()
    open(SITES_PATH_PATH, 'w').write(sites_path)
    





