#!/usr/bin/python3

import sys
import serial
import time
import struct
# readchar is required for the command line version
# install through pip3 
import readchar

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=5)

# read from Arduino
in_put = ser.read()
# Initial response is 255 = ready to send
ser.write(struct.pack('B',255))

quizzes = [
        [3,2,4,1,3,1],
        [1,1,3,1,2,1],
        [1,2,2,1,4,4]
        ]

answers = [0,0,0,0,0,0]

quiz_number = 0


# Checks against question
#  if >= 100 then subtract 100 and return that as status instead
def check_value (i) :
        if (answers[i] == 0) : return 0
        if (answers[i] >= 100) : return (answers[i] - 100)
        if (quizzes[quiz_number][i] == answers[i]) : return 1
        else : return 2
        

def send_recv () :
        # write something back
        ser.write(struct.pack('B',254))
        for i in range (0,6):
                write_val = check_value(i)
                #print ("Returning " + str(i) + ": " + str(write_val))
                ser.write(struct.pack('B',write_val));

        timer = 0;
        # Now clear read buffer until get 254
        while 1:
                if (ser.inWaiting() == 0) :
                        timer +=1
                        if (timer == 10) :
                                ser.write(struct.pack('B',255))
                                timer = 0
                                break
                        print (".", end="")
                        time.sleep (1)
                        continue
                in_put = ser.read()
                in_put_number = ord(in_put)
                # print ("Clearing buffer " + str(in_put_number))
                if (in_put_number == 255) : 
                        ser.write(struct.pack('B',255))
                        continue
                if (in_put_number == 254) : 
                        break
		

        print ("")
        # read response back from Arduino
        for i in range (0,6):
                if (ser.inWaiting() == 0) :
                        timer +=1
                        if (timer == 10) :
                                ser.write(struct.pack('B',255))
                                timer = 0
                                break
                        print (".", end="")
                        time.sleep (1)
                        continue

                in_put = ser.read()
                in_put_number = ord(in_put)
                #print ("Question " + str(i+1) + " answer: " + str(in_put_number) + " should be " +str(quizzes[quiz_number][i]))
                answers[i] = in_put_number




# Used to set timeout
timer = 0;

send_recv();

while 1:
        while 1:
                in_string = input ("Please select a quiz (1-3):")
                if (in_string == '1'):
                        quiz_number = 0
                        break
                if (in_string == '2'):
                        quiz_number = 1
                        break
                if (in_string == '3'):
                        quiz_number = 2
                        break
        print ("Selected quiz: " + str(quiz_number+1))

        # >= 100 then status is returned -100
        # First send blue for all chars
        answers = [103,103,103,103,103,103]
        send_recv()
        

        # Now send updated colour
        print ("Showing result:")
        for i in range (0, 6):
                print ("Question " + str(i+1) + " answer: " + str(answers[i]) + " should be " +str(quizzes[quiz_number][i]))
        send_recv()
        time.sleep(20)
        
        # set back to blank
        answers = [100,100,100,100,100,100]
        send_recv()
        
        
        

