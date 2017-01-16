// Networking Quiz


#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

// NeoPixel Setup
// Which pin on the Arduino is connected to the NeoPixels?
#define PIN            10
// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS      12
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int delayval = 50; // delay for half a second

// 2D array. Each row is a question, 0 = Q pin, 1-4 = answer pins
int quiz_pins[6][5] = {{47,41,40,39,38},{46,39,38,37,36},{45,35,34,33,32},{44,31,30,29,28},{43,27,26,25,24},{42,23,22,21,20}};

// Serial communications setup
int answerStatus[6] = {0,0,0,0,0,0};    // which value sent
int inByte = 0;         // incoming serial byte
int ledStatus[6] = {0,0,0,0,0,0};
int commStatus = 0;    // used for debug


void setup() {
  pixels.begin(); // This initializes the NeoPixel library.
  
  setStatus (11,1);
  
  
  // Setup pins
  // first are set to output with high (use low for enable to check against pull-up)
  // next 4 entries are inputs with pullup
  for (int qnum=0; qnum<6; qnum++) {
        // set 
        pinMode (quiz_pins[qnum][0], OUTPUT);
        digitalWrite(quiz_pins[qnum][0], HIGH);
        for (int anum=1; anum <5; anum++) {
          pinMode(quiz_pins[qnum][anum], INPUT_PULLUP);
        }
      }
  
  
    // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  establishContact();  // send a byte to establish contact until receiver responds 
    
  setStatus (11, 2);
}

void loop() {
  communicate();
  
  setStatus (11,3);
  
  for (int i=0; i<6; i++) {
    setStatus (i, ledStatus[i]+1);
  }
  
  delay(delayval);
  
}


void communicate () {
  while (1) {
      if (Serial.available() > 0) {
      // wait until receive 254
      inByte = Serial.read();
      
      // If we get a 255 - then reset
      if (inByte == 255) {
        setStatus (11, 2);
        return;
      }
      
      if (inByte != 254) continue;
      
      // Must have received 254 - so read next 6 values
      // wait until 6 received
      while (Serial.available() < 6) delay (50);
      for (int i=0; i<6; i++) {
          ledStatus[i] = Serial.read();
      }
      
      Serial.write(254);
      // Get status of each question and write it back
      for (int qnum=0; qnum<6; qnum++) {
        // set to low - so can read inputs
        digitalWrite(quiz_pins[qnum][0], LOW);
        answerStatus[qnum] = 0;
        for (int anum=1; anum <5; anum++) {
           if (digitalRead(quiz_pins[qnum][anum]) == LOW) {
             answerStatus[qnum] = anum;
             break;
           }
        }
        digitalWrite(quiz_pins[qnum][0], HIGH);
        // Write this back to the host computer
        Serial.write(answerStatus[qnum]);
      }
    
 /*     Serial.write(254);
      Serial.write(0);  
      Serial.write(0);
      Serial.write(34);
      Serial.write(35);
      Serial.write(36);
      Serial.write(37);*/
      
      break;
    }  
    
  }
}


// set led - status 0 = off, 1 = green, 2 = red, 3 = blue (searching)
void setStatus (int lednum, int status) {
 switch (status) {
  case 0: pixels.setPixelColor(lednum, pixels.Color(0,0,0));
          break;
  case 1: pixels.setPixelColor(lednum, pixels.Color(0,150,0));
          break;
  case 2: pixels.setPixelColor(lednum, pixels.Color(150,0,0));
          break;
  case 3: pixels.setPixelColor(lednum, pixels.Color(0,0,150));
          break;
  // default invalid - so give a unusual value
  default:pixels.setPixelColor(lednum, pixels.Color(150,150,0));
          break;
 }
 pixels.show();
}


void establishContact() {
  setStatus (0, 0);
  while (1) {
    Serial.write(255);   // send an initial string
    delay(300);
    // read and check for a 255 indicating that the pi is ready
    if (Serial.available() > 0) {
      inByte = Serial.read();
      commStatus = 1 - commStatus;
      setStatus (0, commStatus);
      if (inByte == 255) { 
        return;
      }
      //Serial.write(inByte);
    }
  }
}
