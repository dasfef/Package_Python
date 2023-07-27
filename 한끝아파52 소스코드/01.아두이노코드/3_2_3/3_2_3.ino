#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11
#define VR_PIN  A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int vrValue = analogRead(VR_PIN);
  int percent = map(vrValue,0,1023,0,100);
  Serial.println(percent);

  ledBrightSet(percent);
}

void ledBrightSet(int percentValue)
{
  if (percentValue >= 0 && percentValue <= 10)
  {
    analogWrite(LED_RED, 0);
    analogWrite(LED_GREEN, 0);
    analogWrite(LED_BLUE, 0);
  }
  else if (percentValue >= 11 && percentValue <= 40)
  {
    analogWrite(LED_RED, 80);
    analogWrite(LED_GREEN, 80);
    analogWrite(LED_BLUE, 80);
  }
  else if (percentValue >= 41 && percentValue <= 71)
  {
    analogWrite(LED_RED, 160);
    analogWrite(LED_GREEN, 160);
    analogWrite(LED_BLUE, 160);
  }
  else if (percentValue >= 71 && percentValue <= 100)
  {
    analogWrite(LED_RED, 255);
    analogWrite(LED_GREEN, 255);
    analogWrite(LED_BLUE, 255);
  }
}
//3_2_3.ino
