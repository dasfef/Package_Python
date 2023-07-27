#include <Adafruit_MLX90614.h>
#include <TM1637TinyDisplay.h>

#define PIEZO_BUZZER  3

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

#define CLK 9
#define DIO 10
TM1637TinyDisplay display(CLK, DIO);

float calibrationValue = 5.5;

void setup() {
  Serial.begin(9600);

  mlx.begin();

  display.setBrightness(BRIGHT_7);
}

void loop() {
  float objectTempC = objectTemp();
  if(objectTempC != 0)
  {
    Serial.println(objectTempC);
    if(objectTempC >= 34)
    {
      if(objectTempC <=38.0)
      {
        display.showNumber(objectTempC);
        tone(PIEZO_BUZZER, 1000,500);
      }
      else
      {
        display.showNumber(objectTempC);
        for(int i=0;i<10;i++)
        {
          tone(PIEZO_BUZZER, 800);
          delay(500);
          tone(PIEZO_BUZZER, 1000);
          delay(500);
        }
        noTone(PIEZO_BUZZER);
      }
    }
  }
}

float objectTemp()
{
  static unsigned long currTime = 0;
  static unsigned long prevTime = 0;

  currTime = millis();
  if (currTime - prevTime >= 500)
  {
    prevTime = currTime;
    float ambientTemp = mlx.readAmbientTempC();
    float objectTemp = mlx.readObjectTempC();
    objectTemp = objectTemp + calibrationValue;
    return objectTemp;
  }
  return 0;
}
