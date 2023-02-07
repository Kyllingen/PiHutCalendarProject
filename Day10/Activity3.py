#Beam breaking game. Check how many times beam can be broken
#against a target score

#Imports
from machine import Pin, PWM
import time, sys

#LEDS
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

#Beam
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

#Buzzer
buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

#Game variables
startTime = 0
timeCheck = 0
scoreCounter = 0
state = 0
targetScore = 100

#Game starts after long beep
print("Game starts after the beep!")
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")
print("--------------------------------")

startTime = time.time()

while True:
    
    time.sleep(0.0001)
    
    timeCheck = time.time() - startTime
    
    #Game is over
    if timeCheck >= 30:
        
        red.value(0)
        amber.value(0)
        green.value(0)
        
        buzzer.duty_u16(10000)
        time.sleep(2)
        buzzer.duty_u16(0)
        
        print("-------------------------------")
        print("GAME OVER! YOU LOSE:(")
        print("The target was ", scoreCounter,", you scored ", scoreCounter)
        print("-------------------------------")
        
        sys.exit()
    
    #target score achieved. Game Won
    elif scoreCounter >= targetScore:
        
        red.value(0)
        amber.value(0)
        green.value(0)
        
        buzzer.duty_u16(10000)
        time.sleep(2)
        buzzer.duty_u16(0)
        
        print("-------------------------------")
        print("YOU WIN!")
        print("You took ",timecheck," seconds!")
        print("-------------------------------")
        
        sys.exit()
        
    #Game is still progressing, check against targetScore
    elif state == 0 and beam.value() == 0:
        
        scoreCounter += 1
        
        state = 1
        
        print("SCORE =", scoreCounter, ",",taretScore)
        print("Time remaining:", (30-timeCheck))
        
        # Check which LEDS should show based on current score
        if scoreCounter < (targetScore / 100 * 33)
            
            red.value(1)
            amber.value(0)
            green.value(0)
        
        elif (targetScore / 100 * 33) < scoreCounter < (targetScore / 100 * 66):
            
            red.value(1)
            amber.value(1)
            green.value(0)
            
        else
            
            red.value(1)
            amber.value(1)
            green.value(1)
    
    #Game is still going, score counted - reset state to keep counting
    elif state == 1 and beam.value() == 1:
        state = 0