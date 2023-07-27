#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11

void setup() {
}

void loop() {
  analogWrite(LED_RED,255);
  analogWrite(LED_GREEN,0);
  analogWrite(LED_BLUE,0);
  delay(1000);
  analogWrite(LED_RED,255);
  analogWrite(LED_GREEN,125);
  analogWrite(LED_BLUE,0);
  delay(1000);
  analogWrite(LED_RED,255);
  analogWrite(LED_GREEN,255);
  analogWrite(LED_BLUE,0);
  delay(1000);
  analogWrite(LED_RED,0);
  analogWrite(LED_GREEN,255);
  analogWrite(LED_BLUE,0);
  delay(1000);
  analogWrite(LED_RED,0);
  analogWrite(LED_GREEN,0);
  analogWrite(LED_BLUE,255);
  delay(1000);
  analogWrite(LED_RED,0);
  analogWrite(LED_GREEN,125);
  analogWrite(LED_BLUE,255);
  delay(1000);
  analogWrite(LED_RED,125);
  analogWrite(LED_GREEN,0);
  analogWrite(LED_BLUE,255);
  delay(1000);
}
//2_2_3.ino
