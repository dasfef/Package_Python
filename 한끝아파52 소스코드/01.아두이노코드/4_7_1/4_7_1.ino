void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("VR=?") != -1)
    {
      Serial.println("vr response");
    }
    else if(strRead.indexOf("BRIGHT=?") != -1)
    {
      Serial.println("bright response");
    }
  }
}
//4_7_1.ino
