import board
import busio
import adafruit_bmp280
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True:
    temp = round(sensor.temperature, 2)
    print("Temperature: " + str(temp) + " °C")
    time.sleep(2)