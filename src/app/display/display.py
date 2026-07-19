from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

CHAR_WIDTH = 8
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64

i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21)
)

display = SSD1306_I2C(
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    i2c
)