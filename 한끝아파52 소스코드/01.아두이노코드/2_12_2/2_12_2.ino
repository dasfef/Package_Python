#define LED_RED 5

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED,OUTPUT);
}

void loop() {
  Serial.println("hello");
  delay(1000);
  digitalWrite(LED_RED,HIGH);
  delay(500);
  digitalWrite(LED_RED,LOW);
  delay(500);
}
//2_12_2.ino
