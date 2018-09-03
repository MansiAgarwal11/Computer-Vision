from PIL import Image, ImageChops
import sys
import os

f = sys.argv[1] #image folder


def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
	diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
		return im.crop(bbox)


images = [img for img in os.listdir(f) if img.endswith(".jpg")]
l = len(images)
for i in range(l):
	im = Image.open(f+ "/" + images[i])
	im = trim(im)
	im.save(f+ "/" + images[i])

