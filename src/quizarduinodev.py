import sys
import time
import struct

# This is for testing / development purposes only
# Allows to test on a computer that doesn't have an arduino connected
# All references to serial removed and default responses


class QuizArduino():


    # constructor - does not connect
    def __init__(self, serialDevice, speed=9600, timeout=5):
        self.serialDevice = serialDevice
        self.speed = speed
        self.timeout = timeout

    def connect(self):      
        return True


    # Send list of 6 values for led status and get status of connections
    # LED colours are status 0 = off, 1 = green, 2 = red, 3 = blue (searching)
    def send_recv (self, send_data) :
        return [2,0,2,2,0,1]
