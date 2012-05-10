#!/bin/sh
FILTER=`python config.py brightnessfilter`
IMGDIR=`python config.py imgdir`
kill `cat $IMGDIR/.pidfile`
if [ $FILTER = True ]; then
	mkdir $IMGDIR/filter
	mv $IMGDIR/image*.png $IMGDIR/filter/
	python imagefilter.py $IMGDIR/filter/
	mv $IMGDIR/filter/image*.png $IMGDIR/
fi
cd $IMGDIR
mencoder "mf://image*.png" -o workmovie.mpg -ovc x264
