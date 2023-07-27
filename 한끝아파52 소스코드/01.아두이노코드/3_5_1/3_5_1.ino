#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

float calibrationValue = 5.5;

void setup() {
  Serial.begin(9600);

  mlx.begin();
}

void loop() {
  float objectTempC = objectTemp();
  if(objectTempC != 0)
  {
    Serial.println(objectTempC);
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
