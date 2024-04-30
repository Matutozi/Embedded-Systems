#include "main.h"
//use the remote to select various modes
//security mode, turn on the lights, control the doors, gardens and other parts  of the house
//Connecting the ultrasonic sensor as a starting point of my project.

//pins for the ultrasonic sensor
int trigPin = 12;
int echoPin = 13;
int pingTravelTime;
float pingTravelDistance;
float distance_to_target;
//Pins for the LCD
int rs = 7;
int en = 8;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

//pin for the pir sensor
int pir = 15;

//pin for button state control
int buttonPin = 16;


LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
  digitalWrite(buttonPin, HIGH); //setting the state of the button

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  distance_to_target= measure_distance(); // to get the distance from the h2-sr04 sensor
  display_distance(distance_to_target); // to display the result using the LCD 1602 display

}