#define VR_PIN  A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int vrValue = analogRead(VR_PIN);
  Serial.println(vrValue);
  delay(100);
}
//2_6_1.ino
