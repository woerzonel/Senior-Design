// Load in the libraries
#include <SPI.h>
#include <RF24.h>

// Set the CE & CSN pins
#define CE_PIN   7
#define CSN_PIN 8
#define Sensor 5

// This is the address used to send/receive
const byte rxAddr[6] = "00001";
int numberCount = 0;
int prevNumber = 0;
int savedCount = 0;
int sendFrequency = 100;
// Create a Radio
RF24 radio(CE_PIN, CSN_PIN); 

void setup() {
  
  // Start up the Serial connection
  while (!Serial);
  Serial.begin(9600);
  
  // Start the Radio!
  radio.begin();
  
  // Power setting. Max is the defualt, but make sure it is set since communcation is mean to be at greater distance.
  radio.setPALevel(RF24_PA_MAX); // RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH, RF24_PA_MAX
  
  // Slower data rate for better range, make sure transmitter and reciever match. 
  //radio.setDataRate( RF24_250KBPS ); // RF24_250KBPS, RF24_1MBPS, RF24_2MBPS
  
  // Number of retries and set tx/rx address
  //radio.setRetries(15, 15);
  radio.openWritingPipe(rxAddr);

  // Stop listening, so we can send!
  radio.stopListening();

  //Take the current number
  int prevNumber = digitalRead(Sensor);
}

void loop() {
    //Check the current level of the sensor 1 or 0 (high or low)
    int number = digitalRead(Sensor);
    //The sensor when spinning alternates from high to low or low to high. This means you have to count whenever it changes at all.
    if(number == 0 && prevNumber == 1){

      //We send the information ever 100 roations of the sensor
      //Increase the counter for how frequcently we send information
      numberCount++;
      //Increase total number of rotations the sensor has read.
      savedCount++;
     }
    if(number == 1 && prevNumber == 0){
      //Increase the count of the send frequency
      numberCount++;
      //Increase total number of rotations the sensor has read.
      savedCount++;
    }

    //We decied to go with a set number instead of doing modular division to make it easier to adjust the number as needed. 
    if(numberCount== sendFrequency){
      //The count is converted to a string so it can be sent  
      String count = String(savedCount);
      //The data wouldn't be sent if it was a converted string so it was appened to an empty 
      String str = "";
      str.concat(savedCount);
      //We need to know how many bytes we are sending.
      int str_len = str.length() + 1;
      //We need to covnert the string into a char array cause the bluetooth chip breaks it up and sends it as bytes
      char char_array[str_len];
      str.toCharArray(char_array,str.length()+1);
      //Sendint the information
      radio.write(&char_array, sizeof(char_array));
      //Print the value we send only for testing purposes
      Serial.println(savedCount);
      //Reset the count for frequency
      numberCount = 0;
    }
    prevNumber = number; 
}
