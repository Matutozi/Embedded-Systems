import RPI.GPIO as GPIO
import time

"""Code script that measures the speed of sound using an ultrasonic sensor"""

GPIO.setmode(GPIO.BOARD)

trigPin = 23
echoPin = 24

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def main():
    while True:
        GPIO.output(trigPin, 0)
        time.sleep(2E-6)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)

        while GPIO.input(echoPin) == 0:
            pass
        startTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        stopTime = time.time()

        pingtraveltime = stopTime - startTime

        speedofsound = 16 / pingtraveltime * (3600) / (12 *5280)
        print(f"The speed of sound is {speedofsound} MPH")
        time.sleep(.2)

if __name__ == "__main__":
    main()
