import RPi.GPIO as GPIO
import ADC0834
import dht11
import time
import LCD1602

GPIO.setmode(GPIO.BCM)

buzzPin = 22 #for buzzer pin
tempPin = 26 #for temperature
buttonPin = 24 #for button control


mydht = dht11.DHT11(pin=tempPin)
GPIO.setup(buzzPin, GPIO.OUT)
GPIO.output(buzzPin, GPIO.HIGH) #to turn off the buzzer

ADC0834.setup()
LCD1602.init(Ox27, 1) #1 to turn on the back light

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonState = 1
buttonStateOld = 1

setmode = True # to determine the mode of the system, programming mode OR monitoring mode
buzzVal = 85

def main():
    while True:
        buttonState = GPIO.input(buttonPin)
        print(buttonState)
        if buttonState == 1 and buttonStateOld == 0:
            setmode = not setmode
        print(setmode)
        buttonStateOld = buttonState
        if setmode == True:
            analogVal = ADC0834.getResult()
            buzzVal = int(analogVal * (100/255))
            LCD1602.write(0, 0, "Set Trip Temp: ")
            LCD1602.write(0,1, str(buzzVal))
            time.sleep(.25)
            LCD1602.clear()
            GPIO.output(buzzPin, GPIO.HIGH)

        if setmode == False:
            result = mydht.getResult(0)
            if result.is_valid():
                tempC = result.temperature
                tempF = tempC * 1.8 + 32
                tempF = round(tempF, 1)
                print(buzzVal)
                if tempF < buzzVal:
                    GPIO.output(buzzPin, GPIO.HIGH)

                    LCD1602.write(0,0, "Temp ")
                    #continue it to primt all the other ones
                if tempF >= buzzVal:
                    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(.2)
        LCD1602.clear()
        GPIO.cleanup()
        print("GPIO good to go")