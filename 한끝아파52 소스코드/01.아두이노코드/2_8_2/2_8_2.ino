#include <Servo.h>

#define SERVO_PIN 8
#define VR_PIN  A0

Servo myservo;  

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);  
}

void loop() {
  int setDig = map(analogRead(VR_PIN),0,1023,0,180);
  Serial.println(setDig);
  myservo.write(setDig);
}
//2_8_2.ino
