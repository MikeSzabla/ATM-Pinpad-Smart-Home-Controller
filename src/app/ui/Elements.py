# Parent element class
from app.display.display import DISPLAY_WIDTH, CHAR_WIDTH


class Element:
    """Base class for UI elements on the display."""
    def __init__(self,x,y,selectable=False):
        """Initialize an element at position (x, y).
        
        Args:
            x: Horizontal position in pixels
            y: Vertical position in pixels
            selectable: Whether this element can be selected (default: False)
        """
        self.x = x
        self.y = y
        self.selectable = selectable
        self.neighbors = {}
        self.actions = {}

    def draw(self, display):
        """Draw the element in normal state.
        
        Args:
            display: Display object to render to
        """
        raise NotImplementedError
    
    def draw_selected(self, display):
        """Draw the element in selected state.
        
        Args:
            display: Display object to render to
        """
        raise NotImplementedError
    

# Text Element
class TextElement(Element):
    """Text element for displaying strings on the display."""
    def __init__(self, text, x, y, selectable):
        """Initialize a text element.
        
        Args:
            text: String content to display
            x: Horizontal position in pixels
            y: Vertical position in pixels
            selectable: Whether this element can be selected
        """
        super().__init__(x,y,selectable)
        self.text = text
        self.text_len = len(text)
        
    def draw(self, display):
        """Draw text in normal state (white text on black background).
        
        Args:
            display: Display object to render to
        """
        display.fill_rect(self.x-1, self.y-1, self.text_len*8+2, 10, 0)
        display.text(self.text, self.x, self.y)

    def draw_selected(self, display):
        """Draw text in selected state (black text on white background).
        
        Args:
            display: Display object to render to
        """
        if self.selectable:
            display.fill_rect(self.x-1, self.y-1, self.text_len*8+2, 10, 1)
            display.text(self.text, self.x, self.y, 0)


class Cursor:
    """Manages selection cursor for navigating between elements."""
    def __init__(self, display, element: Element):
        """Initialize cursor on the given element.
        
        Args:
            display: Display object to render to
            element: Element to start cursor on
        """
        self.cur = element
        self.prev = None
        self.cur.draw_selected(display)
        display.show()
    
    def set(self, display, element: Element):
        """Move cursor to a new element.
        
        Args:
            display: Display object to render to
            element: Element to move cursor to
        """
        self.prev = self.cur
        self.cur = element
        self.prev.draw(display)
        self.cur.draw_selected(display)
        display.show()


def x_center(element_width):
    """Calculate x position to center an element horizontally.
    
    Args:
        element_width: Width of element in characters
        
    Returns:
        X pixel position for centered alignment
    """
    return (DISPLAY_WIDTH-element_width*CHAR_WIDTH) // 2