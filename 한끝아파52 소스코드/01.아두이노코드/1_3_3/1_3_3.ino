int ledPin = 13;//정수형 변수 ledPin을 선언하고 초기값13을 저장합니다. 
void setup() { 
  pinMode(ledPin,OUTPUT); //ledPin핀을 출력핀으로 사용하도록 설정합니다.  
}

void loop() {
  digitalWrite(ledPin,HIGH); //ledPin핀을 5V로 출력합니다. 
  delay(1000);               //1000mS 동안 기다립니다
  digitalWrite(ledPin,LOW);  //ledPin핀을 0V로 출력합니다. 
  delay(1000);               //1000mS 동안 기다립니다
}
