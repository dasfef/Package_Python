#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11
#define BUTTON_1 4
#define BUTTON_2 7

int cnt = 0;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
}

void loop() {
  if (btn1() == 1)
  {
    if (cnt < 10)  cnt++;
    Serial.println(cnt);
    ledBrightSet(cnt);
  }
  if (btn2() == 1)
  {
    if (cnt >= 1)  cnt--;
    Serial.println(cnt);
    ledBrightSet(cnt);
  }
}

int btn1()
{
  static int currBtn = 0;
  static int prevBtn = 0;

  currBtn = digitalRead(BUTTON_1);

  if (currBtn != prevBtn)
  {
    prevBtn = currBtn;
    if (currBtn == 1)
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

  if (currBtn != prevBtn)
  {
    prevBtn = currBtn;
    if (currBtn == 1)
    {
      return 1;
    }
    delay(50);
  }

  return 0;
}

void ledBrightSet(int value)
{
  int bright = map(value, 0, 10, 0, 255);
  analogWrite(LED_RED, bright);
  analogWrite(LED_GREEN, bright);
  analogWrite(LED_BLUE, bright);
}
//3_3_2.ino
