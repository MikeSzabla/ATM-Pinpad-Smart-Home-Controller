from app.ui.Elements import TextElement, Cursor, x_center
from app.display.display import display


class RoomsScreen:
    """Screen for selecting a room in the home."""
    def __init__(self):
        """Initialize the Rooms screen with room elements and cursor."""
        self.te_title = TextElement("ROOMS", x_center(5), 0, False)
        self.te_dining_room = TextElement("Dining Room", x_center(11), 15, True)
        self.te_bedroom = TextElement("Bedroom", x_center(7), 30, True)
        self.te_hallway = TextElement("Hallway", x_center(7), 45, True)

        self.te_dining_room.neighbors = {"8": self.te_bedroom}
        self.te_bedroom.neighbors = {"2": self.te_dining_room, "8": self.te_hallway}
        self.te_hallway.neighbors = {"2": self.te_bedroom}


        self.cursor = None

    def render(self):
        """Draw all room screen elements and initialize cursor."""
        self.te_title.draw(display)
        self.te_dining_room.draw(display)
        self.te_bedroom.draw(display)
        self.te_hallway.draw(display)
        display.show()

        self.cursor = Cursor(display, self.te_dining_room)

    def on_keypad_event(self, key):
        """Handle keypad input while this screen is active.
        
        Args:
            key: Key code from keypad
        """

        # hands behavior on directional input
        if self.cursor and key in ["2","4","6","8"] and key in self.cursor.cur.neighbors:
            self.cursor.set(display, self.cursor.cur.neighbors[key])

    
    def cleanup(self):
        """Clean up resources when switching away from this screen."""
        pass
