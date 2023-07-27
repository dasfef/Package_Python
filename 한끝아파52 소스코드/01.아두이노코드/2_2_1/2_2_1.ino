#define LED_RED 5

void setup() {
}

void loop() {
  analogWrite(LED_RED,0);
  delay(1000);
  analogWrite(LED_RED,50);
  delay(1000);
  analogWrite(LED_RED,100);
  delay(1000);
  analogWrite(LED_RED,150);
  delay(1000);
  analogWrite(LED_RED,200);
  delay(1000);
  analogWrite(LED_RED,255);
  delay(1000);
}
//2_2_1.ino
