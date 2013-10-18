python-hosting
==============

Serve multiple wsgi application with nginx and gunicorn.

application isolation
---------------------

One site = one user, every site run on different user.

create new site
---------------

1. create a user 'newuser'
2. `cp sites-available/sample sites-available/newuser`
3. change occurences of 'sample' with 'newuser' and adapt the configs if necessary
4. `cp data/sample data/newuser`, only the files env.sh and app.py are required, they have to be adapted


enable a site
-------------

    python -c "import manage; manage.enable_site(mysite)"
    supervisorctl reload
    nginx reload

disable a site
--------------

    python -c "import manage; manage.disable_site(mysite)"
    supervisorctl reload
    nginx reload




