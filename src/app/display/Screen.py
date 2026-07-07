class Screen:
    def __init__(self, elements):
        self.elements = elements
        self.cursor = next((e for e in elements if e.selectable), None)
        self.dirty = True
    def handle_input(self, ev):
        # translate ev -> neighbor or list move; set dirty when changed
        ...
    def render(self, oled):
        if not self.dirty: return
        oled.fill(0)
        for el in self.elements:
            el.render(oled, el.x, el.y)
        # draw cursor highlight
        oled.show()
        self.dirty = False