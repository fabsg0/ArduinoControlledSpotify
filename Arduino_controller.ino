int stop = 0;
int back = 0;
int next = 0;

void setup() {

  // Declaring the buttons
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);

   
// Initializes the communication between the Arduino and the python script
  Serial.begin(9600);
  Serial.setTimeout(0);
}

void loop() {

  stop = digitalRead(8);
  back = digitalRead(9);
  next = digitalRead(10); 

  
  // If the 'stop' button is pressed, the Arduino sends 'stop' to the python script
  if (stop == HIGH) {
    Serial.println("stop");
    delay(250);
    }

  // If the 'back' button is pressed, the Arduino sends 'back' to the python script
  else if (back == HIGH) {
    Serial.println("back");
    delay(250);
  }

  // If the 'next' button is pressed, the Arduino sends 'next' to the python script
  else if (next == HIGH) {
    Serial.println("next");
    delay(250);
  }
}


