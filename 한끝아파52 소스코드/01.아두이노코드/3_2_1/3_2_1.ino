#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11
#define VR_PIN  A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int vrValue = analogRead(VR_PIN);
  Serial.println(vrValue);
  delay(100);
}
//3_2_1.ino
