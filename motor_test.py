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

def forward(duration):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
 
    # Wait the specified amount of time
    sleep(duration)

    # Stop movement
    stop()
 
def backward(duration):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
 
    # Wait the specified amount of time
    sleep(duration)

    # Stop movement
    stop()
 
def left(duration):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
 
    # Wait the specified amount of time
    sleep(duration)

    # Stop movement
    stop()

def right(duration):
    # Move motors
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
 
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
 
    # Wait the specified amount of time
    sleep(duration)

    # Stop movement
    stop()
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
 
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
