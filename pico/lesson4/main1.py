from machine import Pin
import time

led = Pin("LED", Pin.OUT)
led.value(0)
status = False
while True:
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    time.sleep(1)
print("Hello! python from micropython")