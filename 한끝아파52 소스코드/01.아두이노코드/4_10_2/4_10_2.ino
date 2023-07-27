#include <Servo.h>
#include <TM1637TinyDisplay.h>

#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11
#define SERVO_PIN 8
#define PIEZO_BUZZER  3
#define CLK 9
#define DIO 10
#define BUTTON_1 4
#define BUTTON_2 7

Servo myservo;
TM1637TinyDisplay display(CLK, DIO);

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);
  display.setBrightness(BRIGHT_7);
  pinMode(BUTTON_1, INPUT);
  pinMode(BUTTON_2, INPUT);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("RGB=") != -1)
    {
      int commaIndex1 = strRead.indexOf(",");
      int commaIndex2 = strRead.indexOf(",", commaIndex1 + 1);

      int redValue = strRead.substring(4, commaIndex1).toInt();
      int greenValue = strRead.substring(commaIndex1 + 1, commaIndex2).toInt();
      int blueValue = strRead.substring(commaIndex2 + 1, strRead.length()).toInt();

      redLedSet(redValue, greenValue, blueValue);
      Serial.println("OKRGB");
    }
    else if (strRead.indexOf("SERVO=") != -1)
    {
      int servoDigree = strRead.substring(6, strRead.length()).toInt();
      if (servoDigree <= 180)
      {
        myservo.write(servoDigree);
        Serial.println("OKSERVO");
      }
      else Serial.println("error digree");
    }
    else if (strRead.indexOf("BUZZER=") != -1)
    {
      float bzFreq = strRead.substring(7, strRead.length()).toFloat();
      setBuzzer(bzFreq);
    }
    else if (strRead.indexOf("FND=") != -1)
    {
      float fndValue = strRead.substring(4, strRead.length()).toFloat();
      display.showNumber(fndValue);
      Serial.println("OKFND");
    }
  }

  if(btn1() == 1) Serial.println("BUTTON1=CLICK");
  if(btn2() == 1) Serial.println("BUTTON2=CLICK");
}

void redLedSet(int red, int green, int blue)
{
  analogWrite(LED_RED, red);
  analogWrite(LED_GREEN, green);
  analogWrite(LED_BLUE, blue);
}

void setBuzzer(int freq)
{
  if (freq > 31)
  {
    tone(PIEZO_BUZZER, freq);
    Serial.println("OKBUZZER");
  }
  else
  {
    noTone(PIEZO_BUZZER);
    Serial.println("OKBUZZER");
  }
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
