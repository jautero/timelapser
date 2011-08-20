#!/bin/sh
IMAGEDIR=/var/lib/netf/
mplayer -wid $XSCREENSAVER_WINDOW -loop 0 -fs -mf on:type=png "${IMAGEDIR}/image*.png"


