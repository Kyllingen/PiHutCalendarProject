#Exercise using 1-wire DS18B20 temperature sensor
#Sense the temperature from our found device and use the LEDs
#to indicate the temperature. 

#Imports
import onewire, ds18x20, time
from machine import Pin

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

sensorPin = Pin(26, Pin.IN)

#Tell MicroPython sensor we are using and pin it's on
# then look for the unique rom code on it
sensor = ds18x20.DS18X20(onewire.OneWire(sensorPin))
roms = sensor.scan()

while True:
    
    time.sleep(5)  #must wait at least 1 second for new reading
    
    for rom in roms: # for each sensor found
        sensor.convert_temp()
        time.sleep(1)
        
        reading = sensor.read_temp(rom) 
        print(reading)
        
        if reading <= 18:
            red.value(1)
            amber.value(0)
            green.value(0)
        elif 18 < reading < 22:
            red.value(0)
            amber.value(1)
            green.value(0)
            
        else:
            red.value(0)
            amber.value(0)
            green.value(1)