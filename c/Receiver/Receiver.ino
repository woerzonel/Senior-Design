//#include <SoftwareSerial.h>

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// define the pins
#define CE_PIN   7
#define CSN_PIN 8

//SoftwareSerial BTserial(2, 3);
// Create a Radio
RF24 radio(CE_PIN, CSN_PIN); 

// The tx/rx address 
const byte rxAddr[6] = "00001";

int ledPin = 13;

/**
 *  The set up method run before the loop. It set the defualt settings for the transmitter.
 */
void setup() {
  // Start the serial
  Serial.begin(9600);  //  baud rate 9600 for the serial Bluetooth communication

  
  // Start the radio
  radio.begin();
  
  //Set to change the Baude rate defualt is used. Both Transmitter and reieiver need to match.s
  //radio.setDataRate( RF24_250KBPS ); // RF24_250KBPS, RF24_1MBPS, RF24_2MBPS
  
  // Set the reading pipe and start listening
  radio.openReadingPipe(0, rxAddr);
  radio.setPALevel(RF24_PA_MIN);   // RF24_PA_MIN ,RF24_PA_LOW, RF24_PA_HIGH, RF24_PA_MAX
  radio.startListening();
}
/**
 *  The main method that loops the code inside of it until canceled.
 * The method checks to see if data has been recieived from the transmitter. Then calls the bluetooth method.
 */
void loop() {
  int count = receiver();
  if(count>0){
    bluetooth(count);
  }
}
/**
 *  A method to print out the recieved data to the
 * @param count The data in intager form
 */
void bluetooth(int count){
  Serial.println(String(count));
}

int receiver(){
  //Check to see if the radio is not busy
  if (radio.available()) {
    // Creat a blank array
    char text[32] = "";
    //Reading the messae in from reciever
    radio.read(&text, sizeof(text));
    //Turnin the text into an integer. The print command didn't like a char array.
    int data = atoi(text);   
    return data;
  }
  return -1;
}
