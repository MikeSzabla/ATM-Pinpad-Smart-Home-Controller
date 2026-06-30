from machine import Pin
import time

button = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(5, Pin.OUT)

while True:
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)

    time.sleep(0.1)
