from app.ui.Elements import TextElement, Cursor, x_center
from app.display.display import display


class RoomsScreen:
    """Screen for selecting a room in the home."""
    def __init__(self):
        """Initialize the Rooms screen with room elements and cursor."""
        self.text_title = TextElement("ROOMS", x_center(5), 0, False)
        self.text_dining_room = TextElement("Dining Room", x_center(11), 15, True)
        self.element_bedroom = TextElement("Bedroom", x_center(7), 30, True)
        self.element_hallway = TextElement("Hallway", x_center(7), 45, True)

        self.cursor = None

    def render(self):
        """Draw all room screen elements and initialize cursor."""
        self.text_title.draw(display)
        self.text_dining_room.draw(display)
        self.element_bedroom.draw(display)
        self.element_hallway.draw(display)
        display.show()

        self.cursor = Cursor(display, self.text_dining_room)

    def on_keypad_event(self, key):
        """Handle keypad input while this screen is active.
        
        Args:
            key: Key code from keypad
        """
        pass  # Navigate cursor, trigger actions
    
    def cleanup(self):
        """Clean up resources when switching away from this screen."""
        pass
