#Beam breaking game. Check how many times beam can be broken

#Imports
from machine import Pin, PWM
import time, sys

beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

#Game variables
startTime = 0
timeCheck = 0
scoreCounter = 0
state = 0

print("Game starts after the beep!")

buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")

startTime = time.time()

while True:
    time.sleep(0.0001)
    
    timeCheck = time.time() - startTime
    
    if timeCheck >= 30:
        print("GAME OVER!")
        
        buzzer.duty_u16(10000)
        time.sleep(2)
        buzzer.duty_u16(0)
        
        print("YOUR SCORE: ", scoreCounter)
        
        sys.exit()
    
    elif state == 0 and beam.value() == 0:
        scoreCounter += 1
        
        state = 1
        
        print("SCORE =", scoreCounter)
        print("Time remaining:", (30-timeCheck))
    
    elif state == 1 and beam.value() == 1:
        state = 0