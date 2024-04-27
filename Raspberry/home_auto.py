"""code that sounds alarm when it detects motion in dark room"""

import RPi.GPIO as GPIO
import time
import ADC0834 #for analog to digital conversion

GPIO.setmode(GPIO.BCM)
buzzPin = 26
motionPin = 23

GPIO.setup(buzzPin, GPIO.OUT)
GPIO.output(buzzPin, GPIO.HIGH)

GPIO.setup(motionPin, GPIO.IN)

ADC0834.setup()
time.sleep(3)

def main():
    while True:
        motion = GPIO.input(motionPin)
        lightVal = ADC0834.getResult(0)
        print(f"light Val: {lightVal}")
        print(f"Motion: {motion}")
        time.sleep(.2)
        if motion == 1 and lightVal <= 140:
            GPIO.output(buzzPin, GPIO.LOW)
            print("INTRUDER ALERT")
            print("Deploy counter measures")
        else:
            GPIO.output(buzzPin, GPIO.HIGH)
            print("All clear on the eastern front")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(.12)
        GPIO.cleanup()
        print("GPIO good to go")
