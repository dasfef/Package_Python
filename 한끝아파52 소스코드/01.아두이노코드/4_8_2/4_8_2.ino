#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if (strRead.indexOf("TEMPERATURE=?") != -1)
    {
      sendTemperature();
    }
    else if (strRead.indexOf("HUMIDITY=?") != -1)
    {
      sendHumidity();
    }
  }
}

void sendTemperature()
{
  float temperature = dht.readTemperature();
  if (!isnan(temperature))
  {
    Serial.print("TEMPERATURE=");
    Serial.println(temperature);
  }
  else
  {
    Serial.print("TEMPERATURE=");
    Serial.println(0);
  }
}

void sendHumidity()
{
  float humidity = dht.readHumidity();
  if (!isnan(humidity))
  {
    Serial.print("HUMIDITY=");
    Serial.println(humidity);
  }
  else
  {
    Serial.print("HUMIDITY=");
    Serial.println(0);
  }
}
//4_8_2.ino
