#!/usr/bin/python

import Image,opencv,time,os
from opencv import highgui

def process_images(images):
    datas = [img.load() for img in images]
    width,height=images[0].size
    totfiles=len(images)
    for y in range(0,height):
        for x in range(0,width):
            buf=[pixeldata[x,y] for pixeldata in datas]
            buf.sort() #sort individual pixels
            for i in range(0,totfiles): #write out to buffer
                datas[i][x,y]=buf[i]

#images=[]
camera = highgui.cvCreateCameraCapture(0)
delay=10

index=0

while True:
    start_time=time.time()
    im=highgui.cvQueryFrame(camera)
    print "Took a picture"
    image=opencv.adaptors.Ipl2PIL(im)
    image.save("workpic.jpg")
    os.rename("workpic.jpg","image%03d.jpg" % index)
    index+=1
    delta=time.time()-start_time
    if delta<delay:
        time.sleep(delay-delta)
