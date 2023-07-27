void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("TEMPERATURE=?") != -1)
    {
      Serial.println("temperature response");
    }
    else if (strRead.indexOf("HUMIDITY=?") != -1)
    {
      Serial.println("humidity response");
    }
  }
}
//4_8_1.ino
