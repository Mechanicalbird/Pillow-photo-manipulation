from PIL import Image, ImageFilter
import os


image1 = Image.open('cat1.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('cat1_br.jpg')
