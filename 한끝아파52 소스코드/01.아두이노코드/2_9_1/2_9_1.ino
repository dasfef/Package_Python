#include "DHT.h"

#define DHTPIN 2 
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  delay(2000);
  
  float humi = dht.readHumidity();
  float temp = dht.readTemperature();

  if (!isnan(humi) || !isnan(temp)) 
  {
    Serial.print("Humidity: ");
    Serial.print(humi);
    Serial.print("%  Temperature: ");
    Serial.print(temp);
    Serial.println("C");
  }
}
//2_9_1.ino
