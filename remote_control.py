#!/usr/bin/env python

import RPi.GPIO as GPIO
import asyncio
import websockets
import motor

async def hello(websocket, path):
    while True:
        msg = await websocket.recv()
        print("< {}".format(msg))

        if msg == 'forward':
            motor.forward()

        if msg == 'stop':
            motor.stop()

        if msg == 'right':
            motor.right()

        if msg == 'left':
            motor.left()

        if msg == 'backward':
            motor.backward()

    #greeting = "Hello {}!".format(name)
    #await websocket.send(greeting)
    #print("> {}".format(greeting))


if __name__ == "__main__":
    # Setup motors
    GPIO.setmode(GPIO.BOARD)
    motor.setup()

    # Setup websocket server
    start_server = websockets.serve(hello, '192.168.1.202', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
