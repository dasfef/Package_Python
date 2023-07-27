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
  if(brightValue < 500) ledOn();
  else  ledOff();
}

void ledOn()
{
  digitalWrite(LED_RED,HIGH);
  digitalWrite(LED_GREEN,HIGH);
  digitalWrite(LED_BLUE,HIGH);
}

void ledOff()
{
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_GREEN,LOW);
  digitalWrite(LED_BLUE,LOW);
}
//3_1_2.ino
