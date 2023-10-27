#define PIN_LED 7

unsigned int count;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  int count = 0;
  digitalWrite(7, 0);
  delay(1000);

}
void loop() {
  if(count <= 5) {
    digitalWrite(7, 0);
    delay(100);
    digitalWrite(7, 1);
    delay(100);
    count += 1;
    }
  if(count > 5) {
    while(1) {
      digitalWrite(7, 1);
    }
  }
}
 
