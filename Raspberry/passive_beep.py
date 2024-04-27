import RPi.GPIO as GPIO
import time
"""Code to control a passive buzzer which can control the frequency of sound, use PWM"""
#Control the tone
buzzPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
buzz = GPIO.PWM(buzzPin, 400)
buzz.start(50)

def main():
    while True:
        buzz.ChangeFrequency(100)
        time.sleep(1)
        buzz.ChangeFrequency(400)
        time.sleep(1)
