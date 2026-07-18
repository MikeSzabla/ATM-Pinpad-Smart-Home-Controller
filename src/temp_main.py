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


class TextElement:
    def __init__(self, text, x, y, selectable=False):
        self.selectable = selectable
        self.selected = False
        self.text = text
        self.text_len = len(text)
        self.x = x
        self.y = y
        self.neighbors = {}
        self.actions = {}
    def draw_text(self, display):
        display.fill_rect(0, self.y-1, 128, 9, 0)
        display.text(self.text, self.x, self.y)
    def draw_text_selected(self, display):
        display.fill_rect(0, self.y-1, 128, 9, 1)
        display.text(self.text, self.x, self.y, 0)


element_ok = TextElement("ok", x_center(2), 0)
element_1 = TextElement("First Item", x_center(10), 15)
element_2 = TextElement("Second Item", x_center(11), 30)
element_3 = TextElement("Third Item", x_center(10), 45)

element_list = [element_1, element_2, element_3]
for element in element_list:
    element.draw_text(display)
element_ok.draw_text_selected(display)
display.show()
time.sleep(3)

cur = element_ok
prev = None
for i in range(len(element_list)):
    prev = cur
    cur = element_list[i]
    cur.draw_text_selected(display)
    prev.draw_text(display)
    display.show()
    time.sleep(3)


# keypad = Keypad()
# simulator = SerialKeypadSimulator(keypad)

# while True:

#     simulator.update()
#     events = keypad.update()

#     time.sleep_ms(20)