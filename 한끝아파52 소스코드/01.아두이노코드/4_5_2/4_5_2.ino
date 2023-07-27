#include <TM1637TinyDisplay.h>

#define CLK 9
#define DIO 10

TM1637TinyDisplay display(CLK, DIO);

void setup() {
  Serial.begin(9600);
  display.setBrightness(BRIGHT_7);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("FND=") != -1)
    {
      float fndValue = strRead.substring(4, strRead.length()).toFloat();

      display.showNumber(fndValue);
      Serial.println("OKFND");
    }
  }
}
