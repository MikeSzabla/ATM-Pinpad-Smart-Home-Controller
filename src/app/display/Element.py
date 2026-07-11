class Element:
    def __init__(self, selectable=True, element_type="text"):
        self.selectable = selectable
        self.element_type = element_type
        self.neighbors = {}
        self.actions = {}
        self.draw_props_selected = {}
        self.draw_props_normal = {}
    def render(self, buf, x, y): pass
    def on_activate(self): pass