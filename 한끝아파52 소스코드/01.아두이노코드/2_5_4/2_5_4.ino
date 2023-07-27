#define BUTTON_1 4
#define BUTTON_2 7

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
}

void loop() {
  if(btn1() == 1) Serial.println("button1 click");
  if(btn2() == 1) Serial.println("button2 click");
}

int btn1()
{
  static int currBtn = 0;
  static int prevBtn = 0;
  
  currBtn = digitalRead(BUTTON_1);
  
  if(currBtn != prevBtn)
  {
    prevBtn = currBtn;
    if(currBtn == 1)
    {
      return 1;
    }
    delay(50);
  }

  return 0;
}

int btn2()
{
  static int currBtn = 0;
  static int prevBtn = 0;
  
  currBtn = digitalRead(BUTTON_2);
  
  if(currBtn != prevBtn)
  {
    prevBtn = currBtn;
    if(currBtn == 1)
    {
      return 1;
    }
    delay(50);
  }

  return 0;
}
//2_5_4.ino
