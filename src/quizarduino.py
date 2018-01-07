import sys
import serial
import time
import struct

# Used to communicate with the Arduino
#Todo add better error handling


class QuizArduino():


    # constructor - does not connect
    def __init__(self, serialDevice, speed=9600, timeout=5):
        self.serialDevice = serialDevice
        self.speed = speed
        self.timeout = timeout

    def connect(self):
        self.ser = serial.Serial(self.serialDevice, self.speed, timeout=self.timeout)

        # read from Arduino
        in_put = self.ser.read()
        # Initial response is 255 = ready to send
        self.ser.write(struct.pack('B',255))
        
        return True


    # Send list of 6 values for led status and get status of connections
    # LED colours are status 0 = off, 1 = green, 2 = red, 3 = blue (searching)
    def send_recv (self, send_data) :
        # array to collect response
        answers = []
        # write something back
        self.ser.write(struct.pack('B',254))
        for i in range (0,6):
            write_val = send_data[i]
            #print ("Returning " + str(i) + ": " + str(write_val))
            self.ser.write(struct.pack('B',write_val));

        timer = 0;
        # Now clear read buffer until get 254
        while 1:
            if (self.ser.inWaiting() == 0) :
                timer +=1
                if (timer == 10) :
                    self.ser.write(struct.pack('B',255))
                    timer = 0
                    break
                #print (".", end="")
                time.sleep (1)
                continue
            in_put = self.ser.read()
            in_put_number = ord(in_put)
            # print ("Clearing buffer " + str(in_put_number))
            if (in_put_number == 255) : 
                self.ser.write(struct.pack('B',255))
                continue
            if (in_put_number == 254) : 
                break


        #print ("")
        # read response back from Arduino
        for i in range (0,6):
            if (self.ser.inWaiting() == 0) :
                timer +=1
                if (timer == 10) :
                    self.ser.write(struct.pack('B',255))
                    timer = 0
                    break
                #print (".", end="")
                time.sleep (1)
                continue

            in_put = self.ser.read()
            in_put_number = ord(in_put)
            #print ("Question " + str(i+1) + " answer: " + str(in_put_number) + " should be " +str(quizzes[quiz_number][i]))
            answers.append(in_put_number)
        return answers
