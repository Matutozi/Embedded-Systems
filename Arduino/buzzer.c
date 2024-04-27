#to write a code that controls a active buzzer
#passive buzzer requires pwm signal

string msg = "Pls input your number";
Serial.begin(9600);
pinMode(buzzpin, OUTPUT);

Serial.println(msg);
while (Serial.available() == 0)
{

}

mynum = Serial.parseInt();
if (mynum > 10)
{
    digitalWrite(buzzpin, HIGH);
    delay(2000);
    digitalWrite(buzzpin, LOW);

}

#use analogRead to read value from potentiometer
#for ldr as light increases, resistance reduces.