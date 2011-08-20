#!/bin/sh
IMAGEDIR=/var/lib/netf/
mplayer -loop 0 -fs "mf://${IMAGEDIR}/image*.png"


