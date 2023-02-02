#Simple light sensing using print statements to check values as
#a percentage between 0 (no light) to 100 (max light) 
#Shine light / turn off light and run code to see changes

#imports
from machine import ADC, Pin
from time import sleep

lightsensor = ADC(Pin(26))

light = lightsensor.read_u16()

lightpercent = round(light / 65535 * 100, 1)

print(str(lightpercent) + "%")