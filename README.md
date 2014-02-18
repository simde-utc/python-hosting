python-hosting
==============

Serve multiple wsgi application with nginx and uwsgi.

About
-----

### Application isolation

One site = one user, every site run on different user.


Setup
-----

### Requirements

* nginx
* a web group, nginx have to run under it to serve static files
* python
* uwsgi core under /usr/bin

### Compile uwsgi

    git clone https://github.com/unbit/uwsgi.git
    cd uwsgi
    git tag
    git checkout tags/<tagname>    
    python uwsgiconfig.py --build core

### Compile uwsgi python plugins

    python2 uwsgiconfig.py --plugin plugins/python core python2
    python3 uwsgiconfig.py --plugin plugins/python core python3

### Setup python hosting

Run `./scripts/setup.py`.

Generate nginx configuration `./scripts/make_nginx_conf.py`, the 
configuration will be created in the current directory. Feel free to
update it, then add it to nginx/site-enabled, and be sure nginx run under 
web group. Restart nginx.

Make an init script for uwsgi and activate it, there is an example for
sysvinit: `./uwsgi/init-deb.sh`.

You are ready to enjoy python-hosting !

Manage sites
------------

### create new site

1. create a user 'newuser'
2. `./manage.py newuser create`

### enable a site

`./manage.py newuser enable`

### disable a site

`./manage.py newuser disable`

### check environment

You may want to check if the folder struct and the permissions are well
set for the sites, just run the script `./scripts/check_environment.py`.


