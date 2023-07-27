void setup() {
  pinMode(13,OUTPUT); //13번핀을 출력핀으로 사용하도록 설정합니다.  
}

void loop() {
  digitalWrite(13,HIGH); //13번핀을 5V로 출력합니다. 
  delay(1000);           //1000mS 동안 기다립니다
  digitalWrite(13,LOW);  //13번핀을 0V로 출력합니다. 
  delay(1000);           //1000mS 동안 기다립니다
}
