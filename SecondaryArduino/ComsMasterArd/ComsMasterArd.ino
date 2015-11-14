#include <Wire.h>

// Wire Master Writer
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Writes data to an I2C/TWI slave device
// Refer to the "Wire Slave Receiver" example for use with this

// Created 29 March 2006

// This example code is in the public domain.




void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
}

unsigned int x = 0;
String sendData;
String receivedString;
unsigned int receivedInt;
int comsIndex;
char tempReceive;
void loop() {
  Serial.println(" ");
  Serial.println("Start");
  masterWrite();
  
  delay(250);
  
  masterRequest();
  
  if(x<12000){
    x+=765; }
    else {
      x=0;
    }
  delay(250);
  Serial.println("End");
}


void masterWrite(){
  Serial.print(x);
  Serial.println("write");
  sendData = String(x+10000);
  Serial.print(sendData);
  Serial.println("sent");
  Wire.beginTransmission(8); // transmit to device #8

  Wire.write(sendData.c_str());

  Wire.endTransmission();    // stop transmitting
}

void masterRequest(){
  Serial.println("req");
  receivedString = 0;
  Wire.requestFrom(8,5);
  while (Wire.available()) {
    tempReceive = Wire.read();
    receivedString += tempReceive;
    
  }
  Serial.print(receivedString);
  Serial.println("raw");
  receivedInt = receivedString.toInt();
  receivedInt -= 10000;
  Serial.print(receivedInt);
  Serial.println("fin");
}
