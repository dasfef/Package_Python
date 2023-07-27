void setup() {
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(11,OUTPUT);
}

void loop() {
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(11,LOW);
  delay(1000);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(11,LOW);
  delay(1000);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  digitalWrite(11,HIGH);
  delay(1000);
}
//2_1_3.ino
