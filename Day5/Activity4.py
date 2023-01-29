#Playing with the buzzer to generate sounds using PWM frequency
# and duty (volume) cycle
# Use buzzer to play a small jingle by changing frequency to emulate notes

#Imports
from machine import Pin, PWM, ADC
import time

#Set up buzzer, potentiometer and values
buzzer = PWM(Pin(13))

C = 523
D = 587
E = 659
G = 784


volume = 10000


#Behold the very inefficient way of playing the song
# "Jin..."
buzzer.duty_u16(volume) # Volume up
buzzer.freq(E) # Set frequency to the E note
time.sleep(0.1) # Delay
buzzer.duty_u16(0) # Volume off
time.sleep(0.2) # Delay

# "...gle"
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "Bells"
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.5) # longer delay

# "Jin..."
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "...gle"
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "Bells"
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.5) # longer delay

# "Jin..."
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "...gle"
buzzer.duty_u16(volume)
buzzer.freq(G)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "All"
buzzer.duty_u16(volume)
buzzer.freq(C)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "The"
buzzer.duty_u16(volume)
buzzer.freq(D)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

# "Way"
buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(0)