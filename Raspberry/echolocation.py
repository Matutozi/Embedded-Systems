import RPi.GPIO as GPIO
import time
"""Script that implements the use of h2SR04 ultrasonic sensor"""
GPIO.setmode(GPIO.BCM)

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

        pingTravelTime = stopTime - startTime
        print(pingTravelTime)
        #to convert to microseconds to make it more readable
        print(int(pingTravelTime * 1E6))
        time.sleep(.2) #delay of 0.2 seconds.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")