void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');  // Read message from the client
    message += " - Hi brother!";  // Modify the message
    // digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
    delay(6000);
    digitalWrite(11, LOW);
    Serial.println(message);  // Send modified message back to the client
    
  }
}