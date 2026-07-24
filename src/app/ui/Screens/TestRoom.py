from app.ui.Elements import TextElement, Cursor, x_center
from app.display.display import display


class TestRoomScreen:
    def __init__(self):
        self.te_title = TextElement("TEST ROOM", x_center(5), 1, False)
        self.te_percent = TextElement("100%", x_center(4), 30, True)

        self.cursor = None

    def render(self):
        """Draw all room screen elements and initialize cursor."""
        self.te_title.draw(display)
        self.te_percent.draw(display)
        display.show()

        self.cursor = Cursor(display, self.te_percent)

    def on_keypad_event(self, key):
        """Handle keypad input while this screen is active.

        Args:
            key: Key code from keypad
        """

        # Handle directional input between room options.
        if self.cursor and key in ["2", "4", "6", "8"] and key in self.cursor.cur.neighbors:
            self.cursor.set(display, self.cursor.cur.neighbors[key])

    def cleanup(self):
        """Clean up resources when switching away from this screen."""
        pass