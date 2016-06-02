#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_recording('videos/test.h264')
sleep(2)
camera.stop_recording()
