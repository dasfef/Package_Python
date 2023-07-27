void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("OBJECT=?") != -1)
    {
      Serial.println("object response");
    }
    else if (strRead.indexOf("AMBIENT=?") != -1)
    {
      Serial.println("ambient response");
    }
  }
}
