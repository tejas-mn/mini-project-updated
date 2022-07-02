#include <IRremote.h>

int RECV_PIN = 10; 


IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  pinMode(9,OUTPUT); digitalWrite(9,LOW);// GND
  pinMode(8,OUTPUT); digitalWrite(8,HIGH);//VCC
  Serial.begin(115200);
  
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("Enabled IRin");
}

void loop() {
  if (irrecv.decode()) {
    //Serial.println(results.value, HEX);

//    Serial.print(F("Decoded protocol: "));
//    Serial.print(getProtocolString(irrecv.decodedIRData.protocol));
//    Serial.print(F("Decoded raw data: "));
      Serial.println(irrecv.decodedIRData.decodedRawData, HEX);
//    Serial.print(F(", decoded address: "));
//    Serial.print(irrecv.decodedIRData.address, HEX);
//    Serial.print(F(", decoded command: "));
//    Serial.println(irrecv.decodedIRData.command, HEX);
    irrecv.resume(); // Receive the next value
  }

  
  delay(50);//DELAY FOR STABILITY
}
