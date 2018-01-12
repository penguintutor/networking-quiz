# Networking-quiz

This is a multi-choice quiz with a difference. All the answers are cabled up using patch leads between two CAT-5 patch panels.

This is a project that I created for a careers fair. 
It uses an Arduino Mega which is cabled up to two patch panels, and a string of NeoPixels. This is then controlled by a Raspberry Pi (or other computer) where the user works through the questions one at a time. At the end they are rewarded by appropriate colours on the NeoPixels (green for correct or red for incorrect) and a speedometer display. 

The gui is created using Python 3 and guizero.

This has only limited appeal as it is designed for this one specific task, but the code could be used as a basis for other projects based around an arduino and/or guizero.

[For more details see PenguinTutor Network Quiz](http://www.penguintutor.com/news/stem/network-challenge)

## Install

The first task is to cable up the patch panel and the NeoPixels to the Arduino. The port details are contained within the Arduino code. 

The Arduino needs to be connected to the host computer (Raspberry Pi) using a USB cable, which is then left in place for the computer to Arduino communications.

### Load code onto the Arduino

The code for the Arduino is in the arduino directory and needs to be installed through the Arduino IDE. 

First install the Adafruit NeoPixel library
Go to https://github.com/adafruit/Adafruit_NeoPixel 
from the clone or download button choose download as Zip.

Unzip the file eg. 
unzip Adafruit_NeoPixel-master.zip

cp -r Adafruit_NeoPixel-master/ ~/sketchbook/libraries/
cd ~/sketchbook/libraries
mv Adafruit_NeoPixel-master Adafruit_NeoPixel

Restart the Arduino IDE

Then open the networking_quiz file into the IDE, compile and install it onto the Arduino.


## Python GUI

The quiz is controlled using quiz.py which is contained within the src directory.
There is also an old CLI version within the src directory, which is left for compatibility, but will be removed in future.


## Python modules

The code makes use of pySerial which may need to be installed if not already. This can be achieved using PIP 3.

The code also makes use of guizero, but at the time of writing this requires the development version. In future this should work from version 0.5 of the library. This is easiest installed by downloading from github into a guizero directory in the src directory. Then run python3 setup.py build to create the library.

Once these are met run ./quiz.py from the command line.


## Quiz format

The quiz is defined by a json file in the quizzes directory. The example quiz should be used as a template. All fields must be included for all questions (even if set to blank using ""). This includes details 1 to 6, option 1 to 4, image and answer. The answer starts at zero, so for option A the answer would be 1, for option B it would be 2 etc.

The code will accept any number of questions (within memory constraints).

The corresponding images must be stored within the src\images directory. There are a few generic images provided already, but you may add more if required. You may want to change the logo.gif and quiz.gif images which relate to a logo and the main quiz image respectively.

## More information

For more information see the following links
* [School Computer Fair Networking Quiz](http://www.penguintutor.com/news/stem/network-challenge)
* [Updated Network Quiz Challenge with GUI](http://www.penguintutor.com/news/stem/networking-quiz2)


## Future development

This code is being improved on year-by-year, but most development is in December and January each year only. 
