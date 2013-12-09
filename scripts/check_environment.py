#!/usr/bin/env python

import os
import sys
import pwd
import grp
import re
import traceback

DIR = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(DIR, '..'))
ROOT_CONF = os.path.join(ROOT, 'conf')
SITES_PATH_PATH = os.path.join(ROOT_CONF, 'sites_path.txt')

class ModeException(Exception): pass
class OwnerException(Exception): pass
class TypeException(Exception): pass

def check_mode(path, expected):
    mode = oct(os.stat(path).st_mode & 0o7777)
    if mode != expected:
        raise ModeException('%s expected mode is %s, got %s' % (path, expected, mode))

def _check_uid_or_gid(func_uid, func_nam, func_id, t, path, expected):
    if isinstance(expected, str):
        expected = func_uid(expected)
    id = func_id(path)
    if id != expected:
        expected = func_nam(expected)
        id = func_nam(id)
        raise OwnerException('%s expected %s is %s, got %s' % (path, t, expected, id))

def check_uid(path, expected):
    _check_uid_or_gid(lambda x: pwd.getpwnam(x).pw_uid,
                lambda x: pwd.getpwuid(x).pw_name,
                lambda x: os.stat(path).st_uid,
                'owner', path, expected)

def check_gid(path, expected):
    _check_uid_or_gid(lambda x: grp.getgrnam(x).gr_gid,
                lambda x: grp.getgrgid(x).gr_name,
                lambda x: os.stat(path).st_gid,
                'group', path, expected)

def check_exists(path):
    if not os.path.exists(path):
        raise TypeException('%s does not exist !' % path)

def check_isdir(path):
    if not os.path.isdir(path):
        raise TypeException('%s should be a dir !' % path)

def check_isfile(path):
    if not os.path.isfile(path):
        raise TypeException('%s should be a file !' % path)

def check_directory(path, mode, uid, gid):
    for dirpath,dirnames,filenames in os.walk(path):
        if not re.search('/envpy\d/lib/python\d.\d/?$', dirpath):
            for filename in filenames:
                p = os.path.join(dirpath, filename)
                try:
                    check_uid(path, uid)
                    check_gid(path, gid)
                except Exception as e:
                    #traceback.print_exc()
                    print e


def check_site(path):
    site = path.strip(os.sep).split(os.sep)[-1]
    print 'Check %s %s' % (site, path)
    try:
        check_mode(path, '02755')
        check_uid(path, site)
    except Exception as e:
        #traceback.print_exc()
        print e
    app_dir = os.path.join(path, 'app')
    if not os.path.exists(app_dir):
        print 'Missing app dir'
    else:
        try:
            check_mode(app_dir, '02700')
            check_uid(app_dir, site)
        except Exception as e:
            #traceback.print_exc()
            print e
    static_dir = os.path.join(path, 'static')
    if not os.path.exists(static_dir):
        print 'Missing static dir'
    else:
        try:
            check_mode(static_dir, '02750')
            check_uid(static_dir, site)
        except Exception as e:
            #traceback.print_exc()
            print e
        check_directory(static_dir, '2750', site, 'web')

def check_sites(path):
    for row in os.listdir(path):
        p = os.path.join(path, row)
        if os.path.isdir(p):
            check_site(p)


if __name__ == '__main__':
    sites_path = open(SITES_PATH_PATH).read()
    check_sites(sites_path)
