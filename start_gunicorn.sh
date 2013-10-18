#!/bin/bash

# doit être appellé dans le dossier de l'asso

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ASSO="$(whoami)"

function write
{
	echo "$(date +"%Y-%m-%d %H:%M:%S") [$$] [INFO] $1"
}

source env.sh

write `which python`

exec gunicorn -c "$DIR/gunicorn_conf.py" app:application
