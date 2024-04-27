#use pip3 install dht11 to install the library
import RPi.GPIO as GPIO
import time
import dht11
"""Code script to read the temperature and humidity of an environment using the dht11 sensor"""

GPIO.setmode(GPIO.BCM)
dhtPin = 17
mydht = dht11.DHT11(pin=dhtPin)

def main():
    while True:
        result = mydht.read()
        if result.is_valid():
            print(f"Temperature is {result.temperature}, Humidity is {result.humidity}")
        time.sleep(.2)