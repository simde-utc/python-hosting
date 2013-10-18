import sys
import os
import subprocess

asso = subprocess.check_output('whoami').strip()
ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT_ASSO = os.path.abspath(os.path.join(ROOT, 'sites-enabled', asso))

workers = 3
accesslog = "-" # write access logs in stderr

bind = 'unix:'+os.path.join(ROOT_ASSO, 'wsgi.sock')
pidfile = os.path.join(ROOT_ASSO, 'gunicorn.pid')

additional_conf = os.path.join(ROOT, asso, 'gunicorn_conf.py')
if os.path.isfile(additional_conf):
	execfile(additional_conf, __file__=additional_conf)

