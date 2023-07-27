#define LED_RED 5

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED,OUTPUT);
}

void loop() {
  sayHelloSerial();
  redLedFlash();
}

void sayHelloSerial()
{
  static unsigned long currTime = 0;
  static unsigned long prevTime = 0;
  currTime = millis();
  if(currTime - prevTime >= 1000)
  {
    prevTime = currTime;
    Serial.println("hello");
  }
}

void redLedFlash()
{
  static unsigned long currTime = 0;
  static unsigned long prevTime = 0;
  static int ledState = 0;
  currTime = millis();
  if(currTime - prevTime >= 500)
  {
    prevTime = currTime;
    digitalWrite(LED_RED,ledState);
    ledState = !ledState;
  }
}
//2_12_5.ino
