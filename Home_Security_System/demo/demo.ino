//Connecting the ultrasonic sensor as a starting point of my project.
int trigPin = 12;
int echoPin = 13;
int pingTravelTime;
float pingTravelDistance;
float distance_to_target;
void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
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
  Serial.print("Your distance to the target is: ");
  
  Serial.print(distance_to_target);
  Serial.println(" inches.");
  delay(500);
 

}
