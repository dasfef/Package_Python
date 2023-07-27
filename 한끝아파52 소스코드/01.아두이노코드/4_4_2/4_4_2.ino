#define PIEZO_BUZZER  3

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("BUZZER=") != -1)
    {
      float bzFreq = strRead.substring(7, strRead.length()).toFloat();

      setBuzzer(bzFreq);
    }
  }
}

void setBuzzer(int freq)
{
  if (freq > 31)
  {
    tone(PIEZO_BUZZER, freq);
    Serial.println("OKBUZZER");
  }
  else
  {
    noTone(PIEZO_BUZZER);
    Serial.println("OKBUZZER");
  }
}
//4_4_2.ino
