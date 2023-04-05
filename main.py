from machine import Pin
from machine import ADC
from machine import I2C
from machine import SSD1306_I2C
from ipstw_ku import IKB1_Motor
import time

i2cbus = I2C(scl=Pin(22)), sda=Pin(21), freq=400000)
oled = SSD1306_I2C(128,64, i2cbus)
adc1 = ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)

mt = IKB1_Motor(1)
while 1 :
    oled.fill(0)
    try:
        value = adc1.read()
        volt = value / 4095 * 3300
        temp = (volt - 400) / 15.93
        oled.text("Temp = %d C" %temp, 0, 0)
        oled.show()
        print("Temperature = %d C" %temp)
        if temp >= 30:
            mt.speed(100)
        else:
            mt.speed(0)
    except:
        print("Error reading from ADC")
    time.sleep(10)