#define MOISTURE_PIN A0
#define PH_PIN A4

void setup() {
  Serial.begin(9600);
}

void loop() {
  int moisture = analogRead(MOISTURE_PIN);
  int phRaw = analogRead(PH_PIN);
  float voltage = phRaw * (5.0 / 1023.0);
float pH = 7.0 + ((2.5 - voltage) / 0.18);
  if (pH < 0) {
    pH = 0;
  }

  if (pH > 14) {
    pH = 14;
  }
  Serial.print(moisture);
  Serial.print(",");
  Serial.println(pH, 2);

  delay(2000);
}
