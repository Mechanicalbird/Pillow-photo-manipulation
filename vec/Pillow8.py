from PIL import Image
import numpy as np
import os

#im = Image.open('cat1.jpg')
#im.show()

file = open("all-data2.txt", "w")

size_300 = (300,300)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
       i= Image.open(f)
       fn, fext = os.path.splitext(f)


       
       # we want np shape = (3, 300, 300)

       pixels = list(i.getdata()) # (3, 90000)
       width, height = i.size
       pixels = [pixels[j * width:(j + 1) * width] for j in xrange(height)] # (3, 300, 300)

       x_train = np.array(pixels)
       x = x_train[0:300,0:300]
       print x.shape


file.close()




