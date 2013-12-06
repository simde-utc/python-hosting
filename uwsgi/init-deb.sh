#!/bin/sh

### BEGIN INIT INFO
# Provides:          uwsgi
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the uwsgi app server
# Description:       starts uwsgi app server using start-stop-daemon
### END INIT INFO

PATH=/opt/uwsgi:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/uwsgi

OWNER=uwsgi

NAME=uwsgi
DESC=uwsgi

test -x $DAEMON || exit 0

# Include uwsgi defaults if available
#if [ -f /etc/default/uwsgi ] ; then
#        . /etc/default/uwsgi
#fi

set -e

. /lib/lsb/init-functions

DAEMON_OPTS="-d /var/log/uwsgi.log /usr/local/python-hosting/uwsgi/conf/emperor.ini"

case "$1" in
  start)
        echo -n "Starting $DESC: "
        start-stop-daemon --start --quiet \
                --exec $DAEMON -- $DAEMON_OPTS || echo "fail"
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
        start-stop-daemon --signal 3 --quiet --retry 2 --stop  \
                --exec $DAEMON || echo "fail"
        echo "$NAME."
        ;;
  reload)
        killall -HUP $DAEMON
        ;;
  restart)
        echo -n "Restarting $DESC: "
        start-stop-daemon --signal 3 --quiet --retry 2 --stop \
                --exec $DAEMON
        sleep 1
        start-stop-daemon --start --quiet --pidfile /var/run/$NAME.pid \
               --exec $DAEMON -- $DAEMON_OPTS
        echo "$NAME."
        ;;
  status)  
        ps aux | grep -v grep | grep $NAME
        ;;
      *)  
            N=/etc/init.d/$NAME
            echo "Usage: $N {start|stop|restart|reload|status}" >&2
            exit 1
            ;;
    esac
    exit 0
