rom PIL import Image
import numpy as np
import os

#im = Image.open('cat1.jpg')
#im.show()

file = open("all-data.txt", "w")

size_300 = (300,300)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
       i= Image.open(f)
       fn, fext = os.path.splitext(f)

       i.thumbnail(size_300)
       i.save('vectors/{}_300{}'.format(fn, fext))

       im = Image.open('vectors/{}_300{}'.format(fn, fext))
#       im.show()
       
       file.write("new cat")
       file.write("\n")

       for pixel in iter(im.getdata()):
           print pixel
           file.write(str(pixel))
           file.write("\n")
       


file.close()
