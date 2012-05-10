#!/bin/sh

cd `python config.py imgdir`
mencoder "mf://image*.png" -o workmovie.mpg -ovc x264

