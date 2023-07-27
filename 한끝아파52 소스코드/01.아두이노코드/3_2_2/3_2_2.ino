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

  ledBrightSet(vrValue / 4);
}

void ledBrightSet(int value)
{
  if (value >= 20)
  {
    analogWrite(LED_RED, value);
    analogWrite(LED_GREEN, value);
    analogWrite(LED_BLUE, value);
  }
  else
  {
    analogWrite(LED_RED, 0);
    analogWrite(LED_GREEN, 0);
    analogWrite(LED_BLUE, 0);
  }
}
//3_2_2.ino
