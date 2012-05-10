This is some code I wrote to make timelapse video on my netbook.

USAGE
=====

Start shooting timelapse video with `start-timelapse.py`. It will start taking images to configured directory in configured intervals.
It will write a .pidfile to same directory with pid of the process. `stop-timelapse.sh` will use `.pidfile` to kill imaging process and 
then processes images into a mpg video. 

CONFIGURATION
=============

Configuration is done in `config.py` Python file. 

delay
-----
>"How many seconds to wait before taking next picture"

imgdir
------
>"Directory where images taken are stored."

duration
--------
>"How many seconds timelapse shooting should last"

waitkey
-------
>"Wait for user to press enter before taking picture. Usefull for animation."

playsound
---------
>"Play sound after image is taken. For animation made by moving between frames."

brightnessfilter
----------------
>"Run process through `imagefilter.py` script that sorts pixels in images according to brightness."
