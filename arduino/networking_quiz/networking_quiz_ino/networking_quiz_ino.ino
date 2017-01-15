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

void setup() {
  pixels.begin(); // This initializes the NeoPixel library.
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

