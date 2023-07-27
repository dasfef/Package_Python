#define BRIGHT_PIN  A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  int brightValue = analogRead(BRIGHT_PIN);
  Serial.println(brightValue);
  delay(100);
}
//2_7_1.ino
