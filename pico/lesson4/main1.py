from machine import Pin
led = Pin("LED", Pin.OUT)
led.value(1)
print("Hello! python from micropython")