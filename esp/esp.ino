#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;
int16_t ax, ay, az, gx, gy, gz;
int vx = 0;
int vy = 0;
void setup() {
  Serial.begin(115200);

  // Initialize MPU6050
  mpu.initialize();
  if (!mpu.testConnection()) {
    while (1);
  }
}

void loop() {
  // Read gyro data

  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Print gyro data
  Serial.print("Gyro X: ");
  Serial.print(gx);
  Serial.print("  Gyro Y: ");
  Serial.print(gy);
  Serial.print("  Gyro Z: ");
  Serial.println(gz);

  delay(100); // Adjust the delay as needed
}
