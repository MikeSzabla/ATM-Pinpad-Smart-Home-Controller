class Element:
    def __init__(self, selectable=True, kind="text"):
        self.selectable = selectable
        self.kind = kind
        self.neighbors = {}
        self.draw_props_selected = {}
        self.draw_props_normal = {}
    def render(self, buf, x, y): pass
    def on_activate(self): pass