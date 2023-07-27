void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("BUZZER=") != -1)
    {
      float bzFreq = strRead.substring(7,strRead.length()).toFloat();
      Serial.print("Freq:");
      Serial.println(bzFreq);
    }
  }
}
//4_4_1.ino
