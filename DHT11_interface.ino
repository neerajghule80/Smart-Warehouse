#include <SoftwareSerial.h> //Serial library
#include <DHT.h>
 
#define DHTPIN 3  //Where is DHT connected
#define DHTTYPE DHT11  // Type of sensor used
 
/**
 * Arduino connection HC-05 connection: 
 * HC-05  | Arduino
 * TX     | 5
 * RX     | 6
*/
// Here, we exchange them -
//SoftwareSerial bt (5,6);  //RX, TX (Switched on the Bluetooth - RX -> TX | TX -> RX)
int LEDPin = 13; //LED PIN on Arduino
int btdata; // the data given from the computer
 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  //bt.begin(9600);
 
  /* Since we run out of 5v PIN 
  * and don't wanna use a breadboard - the VCC of the DHT11
  * is connected to PIN 8
  * And we just use digitalWrite to put it HIGH
  */
  pinMode(8, OUTPUT); //explained above why PIN 8
  pinMode(2, OUTPUT); //explained above why PIN 8
  pinMode(4, OUTPUT); //explained above why PIN 8
  digitalWrite(8,HIGH);
  digitalWrite(2,HIGH);
  digitalWrite(4,LOW);
  dht.begin();
  Serial.begin(9600);
}
 
void loop() {
    float hh = getHumid();
    float tt = getTemp();
//    Serial.println(hh);
//    Serial.println(tt);
//    Serial.print (String(hh) + "," + String(tt));
    Serial.print (hh);
    Serial.print(",");
    Serial.print(tt);
    Serial.print("\n");
    delay (500); //prepare for data (2s)
}
 
float getHumid() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  return (float)dht.readHumidity();
}
 
float getTemp() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  return (float)dht.readTemperature();
}
