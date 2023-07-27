#define LED_RED 5

unsigned long currTime = 0;
unsigned long prevTime = 0;

unsigned long currTime1 = 0;
unsigned long prevTime1 = 0;
int ledState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED,OUTPUT);
}

void loop() {
  currTime = millis();
  if(currTime - prevTime >= 1000)
  {
    prevTime = currTime;
    Serial.println("hello");
  }
  
  currTime1 = millis();
  if(currTime1 - prevTime1 >= 500)
  {
    prevTime1 = currTime1;
    digitalWrite(LED_RED,ledState);
    ledState = !ledState;
  }
  
}
//2_12_4.ino
