#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);

  mlx.begin();
}

void loop() {
  float ambientTemp = mlx.readAmbientTempC();
  float objectTemp = mlx.readObjectTempC();

  if(objectTemp >= 30.0)
  {
    Serial.print("object: ");
    Serial.print(objectTemp);
    Serial.println("c");
  }
  delay(500);
}
//2_11_2.ino
