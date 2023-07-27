#define VR_PIN  A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int vrValue = analogRead(VR_PIN);
  int percent = map(vrValue,0,1023,0,100);
  Serial.println(percent);
  delay(100);
}
//2_6_2.ino
