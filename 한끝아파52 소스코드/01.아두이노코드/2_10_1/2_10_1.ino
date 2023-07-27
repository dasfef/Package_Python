#include <TM1637TinyDisplay.h>

#define CLK 9
#define DIO 10

TM1637TinyDisplay display(CLK, DIO);

void setup() {
  display.setBrightness(BRIGHT_7);
}

void loop() {
  display.showNumber(1234);
  delay(1000);
  display.showNumber(1.234);
  delay(1000);
  display.showNumber(12.34);
  delay(1000);
  display.showNumber(123.4);
  delay(1000);
  display.showNumber(1234.);
  delay(1000);
}
//2_10_1.ino
