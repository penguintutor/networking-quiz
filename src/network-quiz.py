#!/usr/bin/python3

import serial
import time
import struct

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

# read from Arduino
input = ser.read()
# Initial response is 255 = ready to send
ser.write(struct.pack('B',255))

# Used to set timeout
timer = 0;

while 1:
        # write something back
        #ser.write(b'A') #!b
        ser.write(struct.pack('B',254))
        ser.write(struct.pack('B',3))
        ser.write(struct.pack('B',2))
        ser.write(struct.pack('B',1))
        ser.write(struct.pack('B',0))
        ser.write(struct.pack('B',2))
        ser.write(struct.pack('B',3))

        timer = 0;
        # Now clear read buffer until get 254
        while 1:
                if (ser.inWaiting() == 0) :
                        timer +=1
                        if (timer == 20) :
                                ser.write(struct.pack('B',255))
                                break
                        print (".", end="")
                        time.sleep (1)
                        continue
                input = ser.read()
                input_number = ord(input)
                # print ("Clearing buffer " + str(input_number))
                if (input_number == 255) : 
                        ser.write(struct.pack('B',255))
                        continue
                if (input_number == 254) : 
                        break
		

        # read response back from Arduino
        for i in range (0,6):
                input = ser.read()
                input_number = ord(input)
                print ("Read input back: " + str(input_number))

        time.sleep(5)
