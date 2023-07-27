void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("FND=") != -1)
    {
      float fndValue = strRead.substring(4, strRead.length()).toFloat();

      Serial.print("FND:");
      Serial.println(fndValue);
    }
  }
}
//4_5_1.ino
