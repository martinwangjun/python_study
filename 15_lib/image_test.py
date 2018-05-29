#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
im = Image.open('sample_image01.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
