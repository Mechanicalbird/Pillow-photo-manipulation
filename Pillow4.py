from PIL import Image
import os


image1 = Image.open('cat1.jpg')
image1.rotate(90).save('cat1_mod.jpg')
image1.convert(mode='L').save('cat1_L.jpg')
