#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);

  mlx.begin();
}

void loop() {
  Serial.print("Ambient = "); 
  Serial.print(mlx.readAmbientTempC());
  Serial.print("*C\tObject = "); 
  Serial.print(mlx.readObjectTempC()); 
  Serial.println("*C");

  delay(500);
}
//2_11_1.ino
