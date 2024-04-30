//functions for my home automation system
#include "main.h"

float measure_distance()
{
  int pingTravelTime;
  float pingTravelDistance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pingTravelTime = pulseIn(echoPin, HIGH);
  delay(30);
  pingTravelDistance = (pingTravelTime * 765. * 5280. * 12) / (3600. * 1000000);
  
  distance_to_target = pingTravelDistance / 2;

}

void display_distance(float distance_to_target)
{
  //To display the distance gotten measured by the lcd using the LCD display
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