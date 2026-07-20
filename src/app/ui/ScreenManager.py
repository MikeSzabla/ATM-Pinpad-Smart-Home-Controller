class ScreenManager:
    def __init__(self):
        self.current_screen = None
    
    def switch_to(self, screen):
        if self.current_screen:
            self.current_screen.cleanup()
        self.current_screen = screen()
        self.current_screen.render()
    
    def handle_keypad_event(self, key):
        if self.current_screen:
            self.current_screen.on_keypad_event(key)