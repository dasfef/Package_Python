#define VR_PIN  A0
#define BRIGHT_PIN  A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("VR=?") != -1)
    {
      Serial.print("VR=");
      Serial.println(analogRead(VR_PIN));
    }
    else if(strRead.indexOf("BRIGHT=?") != -1)
    {
      Serial.print("BRIGHT=");
      Serial.println(analogRead(BRIGHT_PIN));
    }
  }
}
//4_7_2.ino
