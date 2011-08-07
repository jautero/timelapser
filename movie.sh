#!/bin/sh

old_count=0

while true; do
    img_count=`ls image*.jpg|wc -l`
    delta=`expr $img_count - $old_count`
    echo $delta
    if [ $delta -gt 24 ]; then 
	mencoder "mf://image*.jpg" -o workmovie.mpg -ovc x264
	kill $!
	mv workmovie.mpg movie.mpg
	mplayer -loop 0 -fs movie.mpg &
	old_count=$img_count
    fi
    sleep 60
done
