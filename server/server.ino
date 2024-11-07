void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
  pinMode(11, OUTPUT); // Set pin 11 as output for LED indicator
  randomSeed(analogRead(0)); // Seed for random choice generation
}

void loop() {
  if (Serial.available() > 0) {
    String playerChoice = Serial.readStringUntil('\n');  

    int aiChoice = random(3);
    String aiChoiceStr;

    if (aiChoice == 0) aiChoiceStr = "rock";
    else if (aiChoice == 1) aiChoiceStr = "paper";
    else aiChoiceStr = "scissors";

    String result;
    if (playerChoice == aiChoiceStr) {
      result = "It's a tie!";
    } else if ((playerChoice == "rock" && aiChoiceStr == "scissors") ||
               (playerChoice == "scissors" && aiChoiceStr == "paper") ||
               (playerChoice == "paper" && aiChoiceStr == "rock")) {
      result = "You win!";
    } else {
      result = "AI wins!";
    }

    String message = "Player chose: " + playerChoice + ", AI chose: " + aiChoiceStr + " - " + result;
    
    digitalWrite(11, HIGH);
    delay(1000);  
    digitalWrite(11, LOW);

    Serial.println(message);
  }
}
