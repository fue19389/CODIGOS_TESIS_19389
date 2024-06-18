#include "BluetoothSerial.h"

BluetoothSerial BT;
#define FORWARD 12
#define RIGHT 14
#define LEFT 27
#define BACKWARD 26
#define STOP 25

int flag = 0;
int count = 0;


void setup() {
  BT.begin("MYESP32E");
  pinMode(FORWARD, OUTPUT);
  pinMode(RIGHT, OUTPUT);
  pinMode(LEFT, OUTPUT);
  pinMode(BACKWARD, OUTPUT);
  pinMode(STOP, OUTPUT);
}

void loop() {
  if (BT.available()) { 
    String datos = BT.readStringUntil('/'); 
    int predict = datos.substring(0, datos.indexOf(',')).toInt(); 
    double lipdif = datos.substring(datos.indexOf(',') + 1).toDouble(); 


    if (lipdif < 0.03) {
    
      if (predict == 0) {
          digitalWrite(LEFT, HIGH);
          digitalWrite(RIGHT, LOW);  
          digitalWrite(BACKWARD, LOW);
          digitalWrite(FORWARD, LOW); 
          digitalWrite(STOP, LOW);
      }
      else if (predict == 1){
          digitalWrite(LEFT, LOW);
          digitalWrite(RIGHT, LOW);  
          digitalWrite(BACKWARD, LOW);
          digitalWrite(FORWARD, LOW); 
          digitalWrite(STOP, LOW);
      }
      else if (predict == 2){
          digitalWrite(LEFT, LOW);
          digitalWrite(RIGHT, HIGH);  
          digitalWrite(BACKWARD, LOW);
          digitalWrite(FORWARD, LOW); 
          digitalWrite(STOP, LOW);
      }
      else if (predict == 3){
          digitalWrite(LEFT, LOW);
          digitalWrite(RIGHT, LOW);  
          digitalWrite(BACKWARD, LOW);
          digitalWrite(FORWARD, HIGH); 
          digitalWrite(STOP, LOW);
      }
      else if (predict == 4){
          digitalWrite(LEFT, LOW);
          digitalWrite(RIGHT, LOW);  
          digitalWrite(BACKWARD, HIGH);
          digitalWrite(FORWARD, LOW); 
          digitalWrite(STOP, LOW);
      }
    }

    else if (lipdif >= 0.03){
          digitalWrite(LEFT, LOW);
          digitalWrite(RIGHT, LOW);  
          digitalWrite(BACKWARD, LOW);
          digitalWrite(FORWARD, LOW); 
          digitalWrite(STOP, HIGH);
  }
 }
}
