from machine import Pin
from config import BUTTONS
from logger import info


class Keypad:

    def __init__(self):
        self.buttons = {}
        self.previous = {}

        for name, gpio in BUTTONS.items():
            pin = Pin(gpio, Pin.IN, Pin.PULL_UP)
            self.buttons[name] = pin
            self.previous[name] = pin.value()

    def update(self):

        events = []

        for name, pin in self.buttons.items():
            current = pin.value()

            if current != self.previous[name]:

                self.previous[name] = current

                if current == 0:
                    print("EVENTS UPDATED")
                    events.append(name)

        return events