#define BRIGHT_PIN  A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  int brightValue = analogRead(BRIGHT_PIN);
  Serial.print(brightValue);
  if(brightValue >=800)
  {
    Serial.println("밝습니다.");
  }
  else if(brightValue < 800 && brightValue >= 500)
  {
    Serial.println("중간입니다.");
  }
  else if(brightValue < 500)
  {
    Serial.println("어둡습니다.");
  }
  delay(100);
}
//2_7_2.ino
