#!/usr/bin/env python

import RPi.GPIO as GPIO
import motor
import distance
from time import sleep

# The distance at which the robot stops.
STOP_DISTANCE = 0.3

# The required distance for the robot to continue once stopped,
RECOVER_DISTANCE = 0.4

# The amount of time for the robot to reverse once it has encounterd
# an object.
BACKPEDDLE_TIME = 0.5
 
if __name__ == "__main__": 
    # Setup
    GPIO.setmode(GPIO.BOARD)
    motor.setup()
    distance.setup()

    try:
        motor.forward()
        while True:
            sleep(0.1)
            dst = distance.get_distance()
            if dst < STOP_DISTANCE:
                #motor.stop()
                #motor.backward(BACKPEDDLE_TIME)
                motor.backward(BACKPEDDLE_TIME)
                motor.left(1)
                #motor.right()
                motor.forward()
                #while dst < RECOVER_DISTANCE:
                #    dst = distance.get_distance()

    except KeyboardInterrupt:
        print('Interuppted, exiting gracefully.')
        GPIO.cleanup()
