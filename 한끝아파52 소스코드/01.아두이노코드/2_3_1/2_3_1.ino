#define PIEZO_BUZZER  3

void setup() {
}

void loop() {
  tone(PIEZO_BUZZER, 261.6); //도
  delay(1000);
  tone(PIEZO_BUZZER, 293.6); //레
  delay(1000);
  tone(PIEZO_BUZZER, 329.6); //미
  delay(1000);
  tone(PIEZO_BUZZER, 349.2); //파
  delay(1000);
  tone(PIEZO_BUZZER, 391.9); //솔
  delay(1000);
  noTone(PIEZO_BUZZER); //끔
  delay(1000);
}
//2_3_1.ino
