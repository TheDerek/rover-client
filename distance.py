#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

TRIG = 31
ECHO = 32

def pulse(port):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(port, GPIO.LOW)

def get_distance(trig=TRIG, echo=ECHO):
    # Trigger a pulse of sound
    pulse(trig)

    # Wait for the pulse to start 
    pulse_start = time.time()
    while GPIO.input(echo) == GPIO.LOW:
        pulse_start = time.time()

    # Wait for the echo to be heard
    pulse_end = time.time()
    while GPIO.input(echo) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance
    distance = pulse_duration * 171.5

    return distance

def setup():
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

if __name__ == "__main__":

    # Setup our inputs and outputs
    GPIO.setmode(GPIO.BOARD)
    setup()

    # Wait for the sensor to settle
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)

    # Print the distance and clean up
    distance = get_distance(TRIG, ECHO)
    print("Distance: " + str(round(distance, 4)) + "m")

    GPIO.cleanup()
