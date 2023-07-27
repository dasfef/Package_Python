#define BUTTON_1 4
#define BUTTON_2 7

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
}

void loop() {
  int bnt_1_value = digitalRead(BUTTON_1);
  int bnt_2_value = digitalRead(BUTTON_2);

  Serial.print(bnt_1_value);
  Serial.print(",");
  Serial.println(bnt_2_value);
  delay(10);
}
//2_5_1.ino
