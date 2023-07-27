#include <TM1637TinyDisplay.h>

#define CLK 9
#define DIO 10

TM1637TinyDisplay display(CLK, DIO);

void setup() {
  display.setBrightness(BRIGHT_7);
}

void loop() {
  display.showString("HELLO");
  delay(1000);
  display.showString("OK");
  delay(1000);
}
//2_10_2.ino
