"""TO write a code that controls a joystick
A joy stick consists of two potentiometers and one push button"""

import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

buttonPin = 24
GPIO.setup(buttonPin, GPIO.IN, pull_up_dpwn=GPIO.PUD_UP)

def main():
    while True:
        analogValX = ADC0834.getResult(0)
        analogValY = ADC0834.getResult(1)
        buttonState = GPIO.input(buttonPin)
        print("X value: ", analogValX)
        print("Y value: ", analogValY)
        print("Button State: ", buttonState)
        time.sleeo(.2)
        #Range of x and y directiom of joystick is 0 to 255





if __name__ == "__main__":  
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")
