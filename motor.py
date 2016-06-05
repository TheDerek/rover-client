#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23
 
def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

def forward(duration=0):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
 
    # Only stop if the user has specified a duration
    if duration > 0:
        # Wait the specified amount of time
        sleep(duration)

        # Stop movement
        stop()
 
 
def backward(duration=0):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)

    # Only stop if the user has specifed a duration
    if duration > 0:
        # Wait the specified amount of time
        sleep(duration)

        # Stop movement
        stop()
 
def left(duration=0):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
 
    if duration > 0:
        # Wait the specified amount of time
        sleep(duration)

        # Stop movement
        stop()

def right(duration=0):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
 
    if duration > 0:
        # Wait the specified amount of time
        sleep(duration)

        # Stop movement
        stop()

def setup():
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
     
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)   

if __name__ == "__main__": 
    GPIO.setmode(GPIO.BOARD)
     
    setup()
     
    print "Going forwards"
    forward(2)
     
    print "Going backwards"
    backward(2)

    print "Left"
    left(2)

    print "Right"
    right(2)
     
    print "Now stop"
    stop() 
     
    GPIO.cleanup()
