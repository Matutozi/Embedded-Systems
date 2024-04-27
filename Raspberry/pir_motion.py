import RPi.GPIO as GPIO
import time

motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
time.sleep(10)

def main():
    while True:
        motion = GPIO.input(motionPin)
        print(motion)
        sleep(.1)