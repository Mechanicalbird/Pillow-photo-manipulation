from PIL import Image
import os


size_300 = (300,300)


for f in os.listdir('.'):
    if f.endswith('.jpg'):
       i= Image.open(f)
       fn, fext = os.path.splitext(f)

       i.thumbnail(size_300)
       i.save('300/{}_300{}'.format(fn, fext))

#image1 = Image.open('cat1.jpg')
#image1.save('cat1.png')
