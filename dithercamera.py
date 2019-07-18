# coding: utf-8

from PIL import Image
import time
import gphoto2 as gp
import RPi.GPIO as GPIO
import os
import logging
import sys
import subprocess

class image_aspect():

    def __init__(self, image_file, aspect_width, aspect_height):
        self.img = Image.open(image_file)
        self.aspect_width = aspect_width
        self.aspect_height = aspect_height
        self.result_image = None

    def change_aspect_rate(self):

        img_width = self.img.size[0]
        img_height = self.img.size[1]

        if img_width > img_height:
            rate = self.aspect_width / img_width
        else:
            rate = self.aspect_height / img_height

        rate = round(rate, 1)
        self.img = self.img.resize((int(img_width * rate), int(img_height * rate)))
        return self

    def past_background(self):
        self.result_image = Image.new("RGB", [self.aspect_width, self.aspect_height], (255, 255, 255, 255))
        self.result_image.paste(self.img, (int((self.aspect_width - self.img.size[0]) / 2), int((self.aspect_height - self.img.size[1]) / 2)))
        return self

    def save_result(self, file_name):
        self.result_image.save(file_name)


if __name__ == '__main__':
    subprocess.call("sudo gphoto2 --capture-image-and-download --force-overwrite --filename ./cap.jpg",shell=True)
    time.sleep(1)

    image_aspect("./cap.jpg",512,384)\
        .change_aspect_rate()\
        .past_background()\
        .save_result('./image1.bmp')

    #subprocess.call("convert -resize 512x384 -gravity center -crop 512x384+0+0 image1.bmp image1.bmp",shell=True)
    check = subprocess.call("convert image1.bmp -rotate 90 -modulate 170 -colorspace Gray  -ordered-dither o4x4 -colors 2 -depth 1 image1.bmp",shell=True)
    #print(check)
    # Image Ptinting
    check = subprocess.call("python2 imageprn.py",shell=True)
    #print(check)

