#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def pulse(port):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(port, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)

TRIG = 40
ECHO = 38

# Setup our inputs and outputs
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Wait for the sensor to settle
GPIO.output(TRIG, GPIO.LOW)
time.sleep(2)

# Trigger a pulse of sound
pulse(TRIG)

# Wait for the pulse to start 
pulse_start = time.time()
while GPIO.input(ECHO) == GPIO.LOW:
    pulse_start = time.time()

# Wait for the echo to be heard
pulse_end = time.time()
while GPIO.input(ECHO) == GPIO.HIGH:
    pulse_end = time.time()

# Calculate the duration of the pulse
pulse_duration = pulse_end - pulse_start

# Calculate the distance
distance = pulse_duration * 17150

# Print the distance and clean up
print("Distance: " + str(round(distance, 2)) + "cm")
GPIO.cleanup()
