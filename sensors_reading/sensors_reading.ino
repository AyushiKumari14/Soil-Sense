// =====================================================
// SMART AGRICULTURE - SOIL MOISTURE + pH SENSOR
// =====================================================

#define MOISTURE_PIN A0
#define PH_PIN A4

void setup() {
  Serial.begin(9600);
}

void loop() {

  // -----------------------------
  // SOIL MOISTURE
  // -----------------------------
  int moisture = analogRead(MOISTURE_PIN);

  // -----------------------------
  // pH SENSOR
  // -----------------------------
  int phRaw = analogRead(PH_PIN);

  // Convert analog value to approximate pH
  // IMPORTANT: This value needs calibration
  float voltage = phRaw * (5.0 / 1023.0);

  float pH = 7.0 + ((2.5 - voltage) / 0.18);

  // Keep pH within normal range
  if (pH < 0) {
    pH = 0;
  }

  if (pH > 14) {
    pH = 14;
  }

  // Send:
  // moisture,pH
  Serial.print(moisture);
  Serial.print(",");
  Serial.println(pH, 2);

  delay(2000);
}
