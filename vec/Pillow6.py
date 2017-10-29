from PIL import Image
import numpy as np
import os

im = Image.open('cat1.jpg')
im.show()

file = open("newfile.txt", "w")

for pixel in iter(im.getdata()):
    print pixel
    file.write(str(pixel))
    file.write("\n")


file.close()

#size_300 = (300,300)
#size_700 = (700,700)

#for f in os.listdir('.'):
#    if f.endswith('.jpg'):
#       i= Image.open(f)
#       fn, fext = os.path.splitext(f)
#
#       i.thumbnail(size_700)
#       i.save('700/{}_700{}'.format(fn, fext))
#
#       i.thumbnail(size_300)
#       i.save('300/{}_300{}'.format(fn, fext))

#image1 = Image.open('cat1.jpg')
#image1.save('cat1.png')
