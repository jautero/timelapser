#!/usr/bin/python

import re, os, sys
import Image, imagesplit

def get_files(src_dir):
  selected=[]
  for file in os.listdir(src_dir):
    if os.path.isfile(os.path.join(src_dir,file)):
      selected.append(file)
  selected.sort()
  return selected

def get_images(src_dir,filenames):
  images=[]
  width=0
  height=0
  for file in filenames:
    print "Reading %s..." % file
    img=Image.open(os.path.join(src_dir,file))
    if width==0:
      width=img.size[0]
    else:
      if width!=img.size[0]:
        raise IOError("Image %s has width %d different from %d" % (file,img.size[0],width))
    if height==0:
      height=img.size[1]
    else:
      if height!=img.size[1]:
        raise IOError("Image %s had height %d different from %d" % (file,img.size[1],height))
    images.append(img)
  return images

def takku_filter_images(images):
  accessors=[img.load() for img in images]
  for x in range(0,images[0].size[0]):
    print "Processing column %d..." % x
    for y in range(0,images[0].size[1]):
      pixelvalues=[img[x,y] for img in accessors]
      pixelvalues.sort()
      for acc,pix in zip(accessors,pixelvalues):
        acc[x,y]=pix

def savefiles(dst_dir,filenames_and_images):
  for file,image in filenames_and_images:
    print "Saving %s..." % file
    image.save(os.path.join(dst_dir,file))

def processor(dir,imagelist):
  img_list=get_images(dir,imagelist)
  takku_filter_images(img_list)
  savefiles(dir,zip(imagelist,img_list))

if __name__=='__main__':
  if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "<source dir>"
    sys.exit(1)

  src=sys.argv[1]
  files=get_files(src)
  splitter=imagesplit.SectionHandler(src,files,processor)
  splitter.ProcessDirectory()
