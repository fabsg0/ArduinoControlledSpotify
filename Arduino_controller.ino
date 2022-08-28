int stop = 0;
int back = 0;
int next = 0;

void setup() {
  
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);

   

  Serial.begin(9600);
  Serial.setTimeout(0);
}

void loop() {

  stop = digitalRead(8);
  back = digitalRead(9);
  next = digitalRead(10); 

  if (stop == HIGH) {
    Serial.println("stop");
    delay(250);
    }

  else if (back == HIGH) {
    Serial.println("back");
    delay(250);
  }

  else if (next == HIGH) {
    Serial.println("next");
    delay(250);
  }
}


