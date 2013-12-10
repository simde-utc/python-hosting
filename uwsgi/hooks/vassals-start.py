#!/usr/bin/env python

import sys
import os
import subprocess

filename = sys.argv[1]
site_name = filename.split('.')[0]
socket_path = "/tmp/uwsgi_%s.sock" % site_name

# change the owner of the socket
subprocess.call(["chown", "%s:web" % site_name, socket_path])

# change the mode
subprocess.call(["chmod", "660", socket_path])


