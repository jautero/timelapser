#!/bin/sh

mencoder "mf://image*.jpg" -o workmovie.mpg -ovc x264
mv workmovie.mpg movie.mpg
mplayer -wid $XSCREENSAVER_WINDOW -loop 0 -fs movie.mpg


