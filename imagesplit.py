import Image, os

class Section:
  def __init__(self,name,x,y):
    self.name=name
    self.x=x
    self.y=y

class SectionHandler:
  MAX_SIZE=64*1024*1024
  SECTIONS=[Section("tl",0,0),Section("tr",1,0),Section("bl",0,1),Section("br",1,1)]
  SCALE=2
  def __init__(self,dir,imagelist,processor):
    self.dir=dir
    self.imagelist=imagelist
    self.processor=processor
    img=Image.open(os.path.join(dir,imagelist[0]))
    self.width=img.size[0]
    self.height=img.size[1]

  def ProcessDirectory(self):
    if (self.width*self.height*len(self.imagelist) < self.MAX_SIZE):
      self.processor(self.dir,self.imagelist)
    else:
      self.SplitImages()
      self.ProcessSubdirs()
      self.JoinImages()
  def SplitImages(self):
    for sec in self.SECTIONS:
      os.mkdir(os.path.join(self.dir,sec.name))
    new_height=self.height/self.SCALE
    new_width=self.width/self.SCALE
    for image in self.imagelist:
      img=Image.open(os.path.join(self.dir,image))
      for sec in self.SECTIONS:
        if sec.x==0:
          xmin=0
          xmax=new_width
        else:
          xmin=new_width
          xmax=self.width
        if sec.y==0:
          ymin=0
          ymax=new_height
        else:
          ymin=new_height
          ymax=self.height
        new_img=img.crop((xmin,ymin,xmax,ymax))
        new_img.save(os.path.join(self.dir,sec.name,image))
  def ProcessSubdirs(self):
    for sec in self.SECTIONS:
      handler=SectionHandler(os.path.join(self.dir,sec.name),self.imagelist,self.processor)
      handler.ProcessDirectory()
  def JoinImages(self):
    new_height=self.height/self.SCALE
    new_width=self.width/self.SCALE
    for image in self.imagelist:
      img=Image.new("RGB",(self.width,self.height))
      for sec in self.SECTIONS:
        new_img=Image.open(os.path.join(self.dir,sec.name,image))
        img.paste(new_img,(sec.x*new_width,sec.y*new_height))
      img.save(os.path.join(self.dir,image))

def unittestprocessor(dir,imagelist):
  pass

if __name__=='__main__':
  import tempfile
  unittestspec=[((100,100),(255,255,255)),((255,255),(255,255,0)),((640,480),(255,0,255)),((800,600),(0,255,255)),((1023,720),(255,0,0))]
  unittestdir=tempfile.mkdtemp()
  print "unittestdir",unittestdir
  testimg=[]
  for spec in unittestspec:
    unitimg=Image.new("RGB",spec[0],spec[1])
    if testimg:
      unitimg.paste(testimg[-1][1],(0,0))
    filename="test-%dx%d.jpg"%spec[0]
    unitimg.save(os.path.join(unittestdir,filename))
    testimg.append((filename,unitimg))
  unittesthandler=SectionHandler(unittestdir,zip(*testimg)[0],unittestprocessor)
  unittesthandler.MAX_SIZE=27
  unittesthandler.ProcessDirectory()
  for imagepair in testimg:
    resultimg=Image.open(os.path.join(unittestdir,imagepair[0]))
    if resultimg.tostring() != imagepair[1].tostring():
      assert "Image %s does not match original!" % imagepair[0]
  import shutil
  shutil.rmtree(unittestdir)
