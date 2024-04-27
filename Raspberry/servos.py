import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pwmPin = 18

GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50) #frequency is 50 hz
pwm.start(0)

def main():
    while True:
        #to get the pwm percent from user
        pwmPercent = float(input("PWM percent: "))
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(.1)
        #2 percent dutycycle: minimum degree change(0)
        #12 percent dutycycle: maximum degree change(180)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO Good to GO")
