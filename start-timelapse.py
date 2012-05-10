#!/bin/python
import time,config,timelapser, os
delay=config.delay
imager=Netf(config.imgdir)
if config.duration != 0:
    end_time=time.time()+duration
else:
    end_time=0
fh=file(os.path.join(config.imgdir,".pidfile"),"w"))
fh.write("%d\n" % os.getpid())
fh.close()
while (end_time==0) or (time.time()>end_time):
    start_time=time.time()
    if config.waitkey:
        raw_input("Press Enter...")
    imager.get_image()
    if config.playsound:
        print "\a"
    delta=time.time()-start_time
    if delta<delay:
        time.sleep(delay-delta)
