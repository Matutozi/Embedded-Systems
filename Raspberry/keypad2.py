"""Code script that uses understands the function of a keypad"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rows = [11,13,15,29] #four gpio pins that conrol the rows
columns = [31,33,35,37] #gpio pins that control the columns

keypad = [[1,2,3,'A'], [4,5,6,'B'], [7,8,9,'C'], ['*',0,'#','D']]
#set up of the output pins
GPIO.setup(rows[0], GPIO.OUT)
GPIO.setup(rows[1], GPIO.OUT)
GPIO.setup(rows[2], GPIO.OUT)
GPIO.setup(rows[3], GPIO.OUT)

#setup for the columns
GPIO.setup(columns[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(columns[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

noPress = True
noPressOld = True
def main():
    while True:
        noPress = True
      #to step through all the buttons
        for myrow in [0,1,2,3]:
            for myColumn in [0,1,2,3]:
                GPIO.output(rows[myrow], GPIO.HIGH)
                buttonVal = GPIO.input(columns[myColumn])
                GPIO.output(rows[myrow], GPIO.LOW)

                if buttonVal == 1:
                    myChar = keypad[myrow][myColumn]
                    #print(myChar)
                    noPress = False
                if buttonVal == 1 and noPress == False and noPressOld == True:
                    print(myChar) #it is saying that you only print a value if the button was pressed and the previous time the 
                                  # button  wasnt pressed
        noPressOld = noPress

        time.sleep(.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")