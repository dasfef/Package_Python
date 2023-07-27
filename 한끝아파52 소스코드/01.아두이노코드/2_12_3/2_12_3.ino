unsigned long currTime = 0;
unsigned long prevTime = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  currTime = millis();
  if(currTime - prevTime >= 1000)
  {
    prevTime = currTime;
    Serial.println("hello");
  }
}
//2_12_3.ino
