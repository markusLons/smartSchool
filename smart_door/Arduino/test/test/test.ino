int MainPin = 9;
void setup() {
  // put your setup code here, to run once:
  pinMode(MainPin, OUTPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(MainPin, HIGH);   // включает светодиод
  delay(20);                  // ждет секунду
  digitalWrite(MainPin, LOW);    // выключает светодиод
  delay(20); 
}
