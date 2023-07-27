#define PIEZO_BUZZER  3

int freq[] = {392,392,440,440,392,392,330,  \
              392,392,330,330,294,          \
              392,392,440,440,392,392,330,  \
              392,330,294,330,262};

int dTime[] = {200,200,200,200,200,200,500, \
              200,200,200,200,1000,        \
              200,200,200,200,200,200,500, \
              200,200,200,200,1000};

void setup() {
}

void loop() {
  for(int i=0;i<sizeof(freq)/sizeof(int);i++)
  {
    tone(PIEZO_BUZZER, freq[i]); delay(dTime[i]);
    noTone(PIEZO_BUZZER); delay(100);
  }
}
//2_3_3.ino
