#control a servos with the potentiometer
import RPi.GPIO as GPIO
import ADC0834 #isstall the module to control the chip
from time import sleep


GPIO.setmode(GPIO.BCM)

pwmPin = 4
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50) #20 ms
pwm.start(0) #0 duty cycle
ADC0834.setup() 

def main():
    while True:
        analogVal = ADC0834.getResult(0) #channel 0
        pwmPercent = 10/155 * (analogVal) + 2
        print(pwmPercent)
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")