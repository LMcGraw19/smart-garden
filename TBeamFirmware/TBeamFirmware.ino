#include <Wire.h> //bme
#include <Adafruit_Sensor.h> //bme
#include <Adafruit_BME280.h> //bme
#include <OneWire.h> //ds18
#include <DallasTemperature.h> //ds18
#include <SHT21.h> //sht21
#include <Adafruit_TSL2591.h> //tsl

#define SEALEVELPRESSURE_HPA (1013.25) //bme

int i; //used throughout the program, this is used to count number of readings taken.

//BME280 variables
Adafruit_BME280 bme;
float airTempArray[5];
float pressureArray[5];
float altitudeArray[5];
float humidityArray[5];

//DS18B20 variables
const int pinUsedByDS18 = 23; //number assigned to this variable = pin on board that the sensor is connected to.
OneWire oneWire(pinUsedByDS18);
DallasTemperature dallasTemp(&oneWire);
float soilTempArray[5];

//SEN0114 variables
const int pinUsedBySEN0114 = 4;
int soilMoistureArray[5];

//SHT21 variables
SHT21 sht;
float airTempArraySHT[5];
float humidityArraySHT[5];

//TSL2591 variables
Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);
int luminosityArray[5];

void setup()
{
  Serial.begin(9600); //used for serial monitor testing purposes
  bme.begin(0x76);
  dallasTemp.begin();
  Wire.begin();
  configureTSL2591(); //function which sets up TSL2591 sensor
}

/*
 *Next function is loop(), which runs continuously from top to bottom. There are three main parts to this function 
 *1 - over the course of ten minutes (controlled by for loop and delay), five readings are taken two minutes apart from each sensor. 
 *        After ten minutes, the for loop condition is not satisfied, thus the code beneath the for loop is executed.
 *2 - for each array where the last five readings are stored, an average reading is calculated. These average results are then stored.
 *3 - These results are then sent via LoRa communication to the database.
 *4 - process repeats from part 1.
 */
 
void loop() 
{
  for (i = 0; i < 5; i++) //when i = 5, loop will break and 10 minutes will have passed
  {
    retrieveBMEReadings();
    retrieveDS18Readings();
    retrieveSEN0114Readings();
    retrieveSHT21Readings();    retrieveTSL2591Readings();
    delay(5000); //will be a two minute delay
    Serial.println();
  }

  //Calculate averages()

  //Send averages to LoRa ()

  //loop will restart from beginning, resetting i = 0 again;

}

void retrieveBMEReadings()
{
  airTempArray[i] = bme.readTemperature();
//  Serial.printf("Picking up a temp of %.2f\n", airTempArray[i]);
  pressureArray[i] = bme.readPressure() / 100.0F;
  altitudeArray[i] = bme.readAltitude(SEALEVELPRESSURE_HPA);
  humidityArray[i] = bme.readHumidity();
}

void retrieveDS18Readings()
{
  dallasTemp.requestTemperatures();
  soilTempArray[i] = dallasTemp.getTempCByIndex(0);
//  Serial.printf("Inserting %.2f into soil temp array\n", soilTempArray[i]);
}

void retrieveSEN0114Readings()
{
  soilMoistureArray[i] = analogRead(pinUsedBySEN0114);
//  Serial.printf("Inserted %d into the soil moisture array\n", soilMoistureArray[i]);
}

void retrieveSHT21Readings()
{
  airTempArraySHT[i] = sht.getTemperature();
  humidityArraySHT[i] = sht.getHumidity();
//  Serial.printf("Inserted %.2f into SHT temperature array, %.2f into SHT humidity array\n", airTempArraySHT[i], humidityArraySHT[i]);
}

void retrieveTSL2591Readings()
{
  luminosityArray[i] = tsl.getLuminosity(TSL2591_VISIBLE);
//   Serial.printf("Inserted %d into luminosity array\n", luminosityArray[i]);
}

void configureTSL2591()
{
  tsl.setGain(TSL2591_GAIN_MED);
  tsl.setTiming(TSL2591_INTEGRATIONTIME_300MS);
}
