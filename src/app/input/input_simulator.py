import sys

from app.config import SIMULATION_ENABLED
from app.infra.logger import info, error


class SerialKeypadSimulator:

    def __init__(self, keypad):
        self.keypad = keypad
        self.enabled = SIMULATION_ENABLED
        self._poller = None

        if not self.enabled:
            return

        try:
            import uselect

            self._poller = uselect.poll()
            self._poller.register(sys.stdin, uselect.POLLIN)
            info("Key simulation enabled. Type commands like: press 7, press enter, press plus")

        except Exception as exc:
            self.enabled = False
            error(f"Disabling key simulation: {exc}")

    def update(self):
        if not self.enabled or self._poller is None:
            return

        if not self._poller.poll(0):
            return

        raw = sys.stdin.readline()
        if not raw:
            return

        raw = raw.strip()
        if not raw:
            return

        button_name = self._parse_button_name(raw)
        if button_name is None:
            info("Simulation command format: press <button>")
            return

        if self.keypad.simulate_press(button_name):
            info(f"Simulated keypress: {button_name}")

    def _parse_button_name(self, raw):
        lower = raw.lower()

        if lower.startswith("press "):
            return lower[6:].strip()

        aliases = {
            "+": "plus",
            "-": "minus",
            "c": "clear",
            "x": "cancel",
            "e": "enter",
            "b": "blank",
        }

        if lower in aliases:
            return aliases[lower]

        if len(lower) == 1 and lower.isdigit():
            return lower

        return None
