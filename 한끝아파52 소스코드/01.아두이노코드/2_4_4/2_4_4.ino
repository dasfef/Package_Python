void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0)
  {
    char readData = Serial.read();
 
    Serial.print("read:");
    Serial.println(readData);
  }
}
//2_4_4.ino
