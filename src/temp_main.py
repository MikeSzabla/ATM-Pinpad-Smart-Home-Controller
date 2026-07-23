from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from app.input.keypad import Keypad
from app.input.input_simulator import SerialKeypadSimulator
import time

CHAR_WIDTH = 8
DISPLAY_WIDTH = 128

i2c = SoftI2C(
    scl=Pin(22),
    sda=Pin(21)
)

display = SSD1306_I2C(
    128,
    64,
    i2c
)

def x_center(element_width):
    return (DISPLAY_WIDTH-element_width*CHAR_WIDTH) // 2

display.fill_rect(0,0,4*8+2,10,1)
display.text("back", 1, 1, 0)
display.show()

# keypad = Keypad()
# simulator = SerialKeypadSimulator(keypad)

# while True:

#     simulator.update()
#     events = keypad.update()

#     time.sleep_ms(20)