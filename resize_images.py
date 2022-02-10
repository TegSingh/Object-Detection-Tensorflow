from PIL import Image
import os, sys

path = '.\\OnlineImages\\'
dirs = os.listdir(path)

def resize():
	for item in dirs:
		print(item)
		if os.path.isfile(path+item):
			print(path+item)
			im = Image.open(path+item)
			f, e = os.path.splitext(path+item)
			imResize = im.resize((512, 512), Image.ANTIALIAS)
			imResize.save(f + '.jpg',  'JPEG', quality=90)

resize()
