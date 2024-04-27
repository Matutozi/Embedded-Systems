"""Learning how to connect the lcs lcd1603 screem using I2C
sudo raspi-config
lsmod | grep i2c (to check if i2c works)
sudo apt-get install i2c-tools
i2cdetect -y 1
sudo apt-get install libi2c-dev
sudo pip3 install smbus2
(Search for the library and add it to the python program folder)

"""

#Code for the lcd display
import time
import LCD1602
LCD1602.init(0x27, 1)

def main():
    while True:
        LCD1602.write(0, 0, "Hello World") #16 columns 2 rows
        LCD1602.write(0, 1, "Welcome!")


if __name__ == "__main__":
    main()
