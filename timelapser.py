#!/usr/bin/python

import Image,opencv,os
from opencv import highgui

class Netf:
    indexstore=".saved_index"
    workimage="workpic.png"
    imagetemplate="image%06d.png"
    def __init__(self,imgdir="/var/lib/netf",camera=0):
        self.camera = highgui.cvCreateCameraCapture(camera)
        self.imgdir=imgdir
        self.index=self.read_index()
    def get_image(self):
        im=highgui.cvQueryFrame(self.camera)
        image=opencv.adaptors.Ipl2PIL(im)
        workimage=os.path.join(self.imgdir,self.workimage)
        imagename=os.path.join(self.imgdir,self.imagetemplate % self.index)
        image.save(os.path.join(self.imgdir,self.workimage))
        os.rename(workimage,imagename)
        self.index+=1
        self.write_index()
    def read_index(self):
        fh=self.get_indexstore_handle("r")
        if fh:
            return int(fh.read())
        else:
            return 0
    def write_index(self):
        fh=self.get_indexstore_handle("w")
        if fh:
            fh.write("%d"%self.index)
            fh.close()
    def get_indexstore_handle(self,mode):
        try:
            return open(os.path.join(self.imgdir,self.indexstore),mode)
        except:
            return None
