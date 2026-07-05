from machine import Pin

from app.config import BUTTONS, VALID_BUTTON_NAMES
from app.infra.logger import error


class Keypad:

    def __init__(self):
        self.buttons = {}
        self.previous = {}
        self._simulated_events = []

        for name, gpio in BUTTONS.items():
            pin = Pin(gpio, Pin.IN, Pin.PULL_UP)
            self.buttons[name] = pin
            self.previous[name] = pin.value()

    def simulate_press(self, button_name):
        if button_name not in VALID_BUTTON_NAMES:
            error(f"Ignoring unknown simulated button: {button_name}")
            return False

        self._simulated_events.append(button_name)
        return True

    def update(self):
        events = self._simulated_events
        self._simulated_events = []

        for name, pin in self.buttons.items():
            current = pin.value()

            if current != self.previous[name]:
                self.previous[name] = current

                if current == 0:
                    events.append(name)

        return events
