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

def main():
    myRow = int(input("Which row to read? "))
    myColumn = int(input("Which column to read? "))
    while True:
        GPIO.output(rows[myRow], GPIO.HIGH)
        butVal = GPIO.input(columns[myColumn])
        GPIO.output(rows[myRow], GPIO.LOW)
        print(butVal)
        time.sleep(.2)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO good to go")