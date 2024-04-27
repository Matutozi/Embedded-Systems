import RPi.GPIO as GPIO
import time
"""Script that implements the use of h2SR04 ultrasonic sensor and calculated the distance in inches"""
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
        start_time = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        stop_time = time.time()
        ping_travel_time = stop_time - start_time
        print(ping_travel_time)
        # TO CALCULATE THE DISTANCE IN inches
        distance = 767 * ping_travel_time * 5280 * 12/3600
        distance = distance / 2
        print(round(distance, 1), "inches")
        time.sleep(.2)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")