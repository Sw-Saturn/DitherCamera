# coding: utf-8

import commands
import time
import gphoto2 as gp
import RPi.GPIO as GPIO
import os
import logging
import sys


if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    callback_obj = gp.check_result(gp.use_python_logging())
    camera = gp.check_result(gp.gp_camera_new())
    gp.check_result(gp.gp_camera_init(camera))
    print('Capturing image')
    file_path = gp.check_result(gp.gp_camera_capture(
        camera, gp.GP_CAPTURE_IMAGE))
    print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    target = os.path.join('/tmp', file_path.name)
    print('Copying image to', target)
    camera_file = gp.check_result(gp.gp_camera_file_get(
        camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
    gp.check_result(gp.gp_file_save(camera_file, target))
    time.sleep(1)
    camera.capture('image.bmp', format = 'bmp', resize=(512, 384))
    check = commands.getoutput("convert foo.bmp -rotate 90 -modulate 170 -colorspace Gray  -ordered-dither o4x4 -colors 2 -depth 1 image1.bmp")
    #print check
    # Image Ptinting
    check = commands.getoutput("sudo python imageprn.py")
    #print check
    gp.check_result(gp.gp_camera_exit(camera))

