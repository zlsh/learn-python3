#-*- coding: utf-8 -*-

__author__ = 'luoshuhan'

from PIL import Image

im = Image.open('/users/luosh/Pictures/b.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((300,150))
im.save('/users/luosh/Pictures/new300150.jpg','PNG')