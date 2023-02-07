#Exercise using 1-wire DS18B20 temperature sensor
#Sense the temperature from our found device and print out result

#Imports
import onewire, ds18x20, time
from machine import Pin

sensorPin = Pin(26, Pin.IN)

#Tell MicroPython sensor we are using and pin it's on
# then look for the unique rom code on it
sensor = ds18x20.DS18X20(onewire.OneWire(sensorPin))
roms = sensor.scan()

while True:
    sensor.convert_temp()
    
    time.sleep(2)  #must wait at least 1 second for new reading
    
    for rom in roms: # for each sensor found
        print((sensor.read_temp(rom)), "C")
        
        time.sleep(5)