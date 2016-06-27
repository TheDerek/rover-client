import lib.xbox as xbox
import time
import motor
import RPi.GPIO as GPIO

# Setup joystick
joy = xbox.Joystick()

# Setup motors
GPIO.setmode(GPIO.BOARD)
motor.setup()

try:
    #Valid connect may require joystick input to occur
    print "Waiting for Joystick to connect"
    while not joy.connected():
        time.sleep(0.10)

    print('Connected')
    #Show misc inputs until Back button is pressed    
    while not joy.Back() and joy.connected():
        if joy.rightTrigger() > 0:
            motor.forward()
        elif joy.leftTrigger() > 0:
            motor.backward()
        elif joy.rightBumper():
            motor.right()
        elif joy.leftBumper():
            motor.left()
        else:
            motor.stop()

finally:
    #Always close out so that xboxdrv subprocess ends
    joy.close()
    print "Done."
