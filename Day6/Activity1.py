#Simple light sensing using print statements to check values
#Shine light / turn off light and run code to see changes

#imports
from machine import ADC, Pin

lightsensor = ADC(Pin(26))

light = lightsensor.read_u16()

print(light)