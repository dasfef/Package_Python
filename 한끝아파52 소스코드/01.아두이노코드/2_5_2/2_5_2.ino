#define BUTTON_1 4
#define BUTTON_2 7

int currBtn = 0;
int prevBtn = 0;
int count = 1;
void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
}

void loop() {
  currBtn = digitalRead(BUTTON_1);
  
  if (currBtn != prevBtn)
  {
    prevBtn = currBtn;
    Serial.print(count);
    Serial.print(":");
    count++;
    Serial.println("button1 click");
    delay(50);
  }
}
//2_5_2.ino
