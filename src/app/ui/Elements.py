# Parent element class
from app.display.display import DISPLAY_WIDTH, CHAR_WIDTH


class Element:
    def __init__(self,x,y,selectable=False):
        self.x = x
        self.y = y
        self.selectable = selectable
        self.neighbors = {}
        self.actions = {}

    def draw(self, display):
        raise NotImplementedError
    
    def draw_selected(self, display):
        raise NotImplementedError
    

# Text Element
class TextElement(Element):
    def __init__(self, text, x, y, selectable):
        super().__init__(x,y,selectable)
        self.text = text
        self.text_len = len(text)
        
    def draw(self, display):
        display.fill_rect(0, self.y-1, 128, 9, 0)
        display.text(self.text, self.x, self.y)

    def draw_selected(self, display):
        if self.selectable:
            display.fill_rect(0, self.y-1, 128, 9, 1)
            display.text(self.text, self.x, self.y, 0)


class Cursor:
    def __init__(self, display, element: Element):
        self.cur = element
        self.prev = None
        self.cur.draw_selected(display)
        display.show()
    
    def set(self, display, element: Element):
        self.prev = self.cur
        self.cur = element
        self.prev.draw(display)
        self.cur.draw_selected(display)
        display.show()


def x_center(element_width):
        return (DISPLAY_WIDTH-element_width*CHAR_WIDTH) // 2