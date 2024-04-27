"""To write a code that uses ldr in a raspberry"""
imoport RPi.GPIO as GPIO
import time
import ADC0834

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

def main():
    while True:
        lightVal = ADC0834.getResult(0)
        print(f"Light val: {lightVal}")
        time.sleep(.2)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(.2)
        GPIO.cleanup()
        print("GPIO go to go")
