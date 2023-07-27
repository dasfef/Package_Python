#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);

  mlx.begin();
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("OBJECT=?") != -1)
    {
      float objectTemp = mlx.readObjectTempC();
      Serial.print("OBJECT=");
      Serial.println(objectTemp);
    }
    else if (strRead.indexOf("AMBIENT=?") != -1)
    {
      float ambientTemp = mlx.readAmbientTempC();
      Serial.print("AMBIENT=");
      Serial.println(ambientTemp);
    }
  }
}
