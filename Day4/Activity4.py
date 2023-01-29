#Play with analog potentiometer using LED lights
#Use PWM (Pulse Width Modulation) signal to fade LED instead of just ON/OFF
#Use Duty Cycle and Frequency to control

#Imports
from machine import ADC, Pin, PWM
import time

#Set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

led = PWM(Pin(18))

#Set how often to switch power between on and off for LED
led.freq(1000)

reading = 0

while True:
    reading = potentiometer.read_u16()
    print(reading)
    
    #Set LED PWM duty cycle to reading value which states
    # how long LED should be on each time
    led.duty_u16(reading)
    
    time.sleep(0.001)