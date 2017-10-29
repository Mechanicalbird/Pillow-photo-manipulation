from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.jpg'):
       i= Image.open(f)
       fn, fext = os.path.splitext(f)
       i.save('pngs/{}.png'.format(fn))

#image1 = Image.open('cat1.jpg')
#image1.save('cat1.png')
