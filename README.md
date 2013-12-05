python-hosting
==============

Serve multiple wsgi application with nginx and uwsgi.

application isolation
---------------------

One site = one user, every site run on different user.

create new site
---------------

1. create a user 'newuser'
2. `./manage.py newuser create`


enable a site
-------------

`./manage.py newuser enable`

disable a site
--------------

`./manage.py newuser disable`




