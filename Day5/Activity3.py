#Playing with the buzzer to generate sounds using PWM frequency
# and duty (volume) cycle
# Use the potentiometer to control the volume of the buzzer

#Imports
from machine import Pin, PWM, ADC
import time

#Set up buzzer, potentiometer and values
buzzer = PWM(Pin(13))
potentiometer = ADC(Pin(27))

reading = 0

while True:
    time.sleep(0.1)
    
    reading = potentiometer.read_u16()
    buzzer.freq(600)
    buzzer.duty_u16(reading)

    print(reading)
