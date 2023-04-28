#include <Servo.h>

Servo myservo;
int angle = 0;
// int ledpin = 3;
const int buttonPin = 2; 
const int servo = 9; 
int buttonState = 0;
String val;

unsigned long startMillis;
unsigned long currentMillis;
const unsigned long period = 43200000;  //120000

void setup() {
  Serial.begin(9600);
  // pinMode(ledpin, OUTPUT);
  myservo.attach(9);
  pinMode(buttonPin, INPUT);
  pinMode(servo,OUTPUT) ;
  startMillis = millis();

}

void loop() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1024.0);
  Serial.println ("Sensor Output (V):");
  Serial.println (sensorValue);
  Serial.println();
  delay(500);

  currentMillis = millis();  
  if (currentMillis - startMillis >= 60000)  
  {  
    for(int i=0;i<18;i++){
      myservo.write(i*10);
      delay(100);
    }
    myservo.write(0);
    startMillis = currentMillis; 
  }

  if(Serial.available()>0) {
    val = Serial.readString();
  }
  else {
    val = "";
  }
  buttonState = digitalRead(buttonPin);
  
  if (buttonState == HIGH) {
    for(int i=0;i<18;i++){
      myservo.write(i*10);
      delay(100);
    }
  } else {
    myservo.write(0);  
  }
  if (val == "s"){
    for(int i=0;i<18;i++){
      myservo.write(i*10);
      delay(100);
    }
    myservo.write(0);
  }

}
