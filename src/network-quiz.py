#!/usr/bin/python3

import serial
import time
import struct

ser = serial.Serial('/dev/ttyACM3', 9600, timeout=5)

# read from Arduino
input = ser.read()
#print ("Read input " + input.decode("utf-8") + " from Arduino")
# Initial response is 255 = ready to send
ser.write(struct.pack('!B',255))

while 1:
        # write something back
        #ser.write(b'A')
        ser.write(struct.pack('!B',254))
        ser.write(struct.pack('!B',3))
        ser.write(struct.pack('!B',2))
        ser.write(struct.pack('!B',1))
        ser.write(struct.pack('!B',0))
        ser.write(struct.pack('!B',2))
        ser.write(struct.pack('!B',3))

        # Now clear read buffer until get 254
        while 1:
                input = ser.read()
                input_number = ord(input)
                print ("Clearing buffer " + str(input_number))
                if (input_number == 255) : 
                        ser.write(struct.pack('!B',255))
                if (input_number == 254) : 
                        break
		

        # read response back from Arduino
        for i in range (0,6):
                input = ser.read()
                input_number = ord(input)
                print ("Read input back: " + str(input_number))
                #print ("Read input back: " + input)

        time.sleep(5)
