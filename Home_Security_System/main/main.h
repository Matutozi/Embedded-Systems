#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <LiquidCrystal.h>
#include <IRremote.h>

float measure_distance(); //calculates the distance using the H2-Sr04
void display_distance(float distance_to_target); //function that displays result on the LCD1602 display
void setupRemote(); // function that control the remote control
bool motion_sensing(); //pir sensor
float temp_monitoring(); //monitors the temperature of the house
bool smoke_sensor(); //returns a value based on some set parameters in the house

#endif
