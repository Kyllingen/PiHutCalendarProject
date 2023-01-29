#Playing with the buzzer to generate sounds using PWM frequency
# and duty (volume) cycle
# Use buzzer to play a small jingle by changing frequency to emulate notes
# Improved version of activity 4 to reduce code length

#Imports
from machine import Pin, PWM, ADC
import time

#Set up buzzer, potentiometer and values
buzzer = PWM(Pin(13))

C = 523
D = 587
E = 659
G = 784


volume = 32768

def playtone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.5)

playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.5)

playtone(E, volume, 0.1, 0.2)
playtone(G, volume, 0.1, 0.2)
playtone(C, volume, 0.1, 0.2)
playtone(D, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)


buzzer.duty_u16(0)