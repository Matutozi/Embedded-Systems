import RPi.GPIO as GPIO

"""
The three modes of the system;
* armed state
* disarmed state
*change password state
"""
GPIO.setmode(GPIO.BOARD) #numbering scheme for the pin selection


PIRpin=12 #pir pin
GPIO.setup(PIRpin,GPIO.IN)

import LCD1602 #library for the LCD operation
import KPLIB # for thr keypad operation
from time import sleep
import threading #to enable a process work in the background
myPad=KPLIB.keypad(retChar='D') #"D is the run key"

LCD1602.init(0x27,1)
myString=''
pwd='1234' #string that stores the password

def readKP():
    """Method that reads from the keypad"""
    global myString
    while myString != '*': #if you type '*' it kills stops reading from the keypady
        myString=myPad.readKeypad() #to read from the keypad
        sleep(.5)

#thread creation
readThread=threading.Thread(target=readKP,) #the function has no attributes
readThread.daemon=True
readThread.start()

while myString != '*': 
    CMD=myString
    if CMD=='A'+pwd:
        LCD1602.write(0,0,'Armed          ')
        moveVal=GPIO.input(PIRpin)
        if moveVal==1:
            LCD1602.write(0,1,'Intruder Alert')
        if moveVal==0:
            LCD1602.write(0,1,'All Clear      ')
    if CMD=='B'+pwd:
        LCD1602.write(0,0,'UnArmed        ')
        LCD1602.write(0,1,'               ')
    if CMD=='C'+pwd:
        LCD1602.write(0,0,'Password?      ')
        LCD1602.write(0,1,'               ')
        while myString=='C'+pwd:
            pass
        pwd=myString
        LCD1602.write(0,0,pwd+'         ')
        sleep(2)
        LCD1602.write(0,0,'               ')
        LCD1602.clear()
sleep(1)
GPIO.cleanup()
LCD1602.clear()
print('GPIO Good to Go')