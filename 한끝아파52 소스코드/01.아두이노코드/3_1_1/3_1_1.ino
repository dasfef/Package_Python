#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11
#define BRIGHT_PIN  A1

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED,OUTPUT);
  pinMode(LED_GREEN,OUTPUT);
  pinMode(LED_BLUE,OUTPUT);
}

void loop() {
  int brightValue = analogRead(BRIGHT_PIN);
  Serial.println(brightValue);
}
//3_1_1.ino
