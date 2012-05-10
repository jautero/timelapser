This is some code I wrote to make timelapse video on my netbook.

USAGE
=====

Start shooting timelapse video with `start-timelapse.py`. It will start taking images to configured directory in configured intervals.
It will write a .pidfile to same directory with pid of the process. `stop-timelapse.sh` will use `.pidfile` to kill imaging process and 
then processes images into a mpg video. 

CONFIGURATION
=============

Configuration is done in `config.py` Python file. 




