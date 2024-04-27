"""To build a temperature and humidity system with the lcd display"""
import RPi.GPIO as GPIO
import DHT11 #to control the humidity sensor
import time
import LCD1602 #to control the led

GPIO.setmode(GPIO.BCM)
myDHT = dht11.DHT11(pin=17)
LCD1602.init(0x27, 1) #1 to turn on the backlight

buttonPin = 21
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonstate = 1
buttonstateold = 1
tmpMode = True #1 stateis farenheint and 0 state is celcius

def main():
    while True:
        buttonstate = GPIO.input(buttonPin)
        if buttonstate == 1 and buttonstateold == 0:
            tmpMode = not tmpMode
        print(tmpMode)
        buttonstateold = buttonstate
        result = myDHT.read()
        tempC = result.temperature
        tempF = tempC * 1.8+32
        hum = result.humidity
        if result.is_valid():
            if tmpMode == True:
                LCD1602.write(0, 0, "Temp")
                LCD1602.write(6,0,str(tempF))
                LCD1602.write(11, "F")
                LCD1602.write(0,1, "Humidity: ")
                LCD1602.write(10, 1, str(hum))
                LCD1602.write(14, 1, "%c")
            if tmpMode == False:
                LCD1602.write(0, 0, "Temp")
                LCD1602.write(6,0,str(tempC))
                LCD1602.write(11, "F")
                LCD1602.write(0,1, "Humidity: ")
                LCD1602.write(10, 1, str(hum))
                LCD1602.write(14, 1, "%c")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(.2)
        GPIO.cleanup()
        LCD1602.clear()
        print("GPIO good to go")
