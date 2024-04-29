#include <LiquidCrystal.h>
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
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pingTravelTime = pulseIn(echoPin, HIGH);
  delay(30);
  pingTravelDistance = (pingTravelTime * 765. * 5280. * 12) / (3600. * 1000000);
  
  distance_to_target = pingTravelDistance / 2;
  //Serial.print("Your distance to the target is: ");
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Target Distance: ");
  lcd.print(distance_to_target);
  lcd.print("  Inches");

  //Serial.print(distance_to_target);
  //Serial.println(" inches.");
  delay(500);
  lcd.clear();  // remove this one to remove the flicker between distance measured

}
