#Playing with the buzzer to generate sounds using PWM frequency
# and duty (volume) cycle
# Play a tone for 1 second

#Imports
from machine import Pin, PWM
import time

#Set up buzzer and values
buzzer = PWM(Pin(13))

buzzer.freq(1000)
buzzer.duty_u16(10000)

time.sleep(1)

buzzer.duty_u16(0)