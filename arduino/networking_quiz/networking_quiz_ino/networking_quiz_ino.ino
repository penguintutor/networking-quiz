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
int delayval = 500; // delay for half a second


// Serial communications setup
int portStatus[6] = {0,0,0,0,0,0};    // which value sent
int inByte = 0;         // incoming serial byte
int ledStatus[6] = {0,0,0,0,0,0};



void setup() {
  pixels.begin(); // This initializes the NeoPixel library.
  
  
    // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  establishContact();  // send a byte to establish contact until receiver responds 
    
}

void loop() {

  // For a set of NeoPixels the first NeoPixel is 0, second is 1, all the way up to the count of pixels minus one.

  for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
    pixels.setPixelColor(i, pixels.Color(150,0,0)); // Moderately bright green color.

    pixels.show(); // This sends the updated pixel color to the hardware.

    delay(delayval); // Delay for a period of time (in milliseconds).

  }
  
  
  
}


void communicate () {
  while (1) {
      if (Serial.available() > 0) {
      // wait until receive 254
      inByte = Serial.read();
      if (inByte != 254) continue;
      
      // Must have received 254 - so read next 6 values
      for (int i=0; i<6; i++) {
          ledStatus[i] = Serial.read();
      }
    
      Serial.write(254);
      Serial.write(0);  
      Serial.write(0);
      Serial.write(34);
      Serial.write(35);
      Serial.write(36);
      Serial.write(37);
    }  
    
  }
}


// set led - status 0 = off, 1 = green, 2 = red, 3 = blue (searching)
void setStatus (int lednum, int status) {
 switch (lednum) {
  case 0: pixels.setPixelColor(lednum, pixels.Color(0,0,0));
          break;
  case 1: pixels.setPixelColor(lednum, pixels.Color(0,150,0));
          break;
  case 2: pixels.setPixelColor(lednum, pixels.Color(150,0,0));
          break;
  case 3: pixels.setPixelColor(lednum, pixels.Color(0,0,150));
          break;
  default:
          break;
 }
}


void establishContact() {
  while (1) {
    Serial.write(255);   // send an initial string
    delay(300);
    // read and check for a 255 indicating that the pi is ready
    if (Serial.available() > 0) {
      inByte = Serial.read();
      if (inByte == 255) return;
      Serial.write(inByte);
    }
  }
}
