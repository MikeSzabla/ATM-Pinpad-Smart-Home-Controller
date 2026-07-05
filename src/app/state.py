class ApplicationState:

    def __init__(self):
        self.current_screen = "rooms"
        self.rooms = []
        self.room_cursor = 0
        self.room_offset = 0
        self.rooms_focus = "list"
        self.selected_room = None
        self.last_error = ""
        self.request_rooms_pending = True
        self.dirty = True

    def mark_dirty(self):
        self.dirty = True

    def clear_dirty(self):
        self.dirty = False

    def set_rooms(self, rooms):
        self.rooms = rooms

        if not self.rooms:
            self.room_cursor = 0
            self.room_offset = 0
            self.selected_room = None
            self.mark_dirty()
            return

        if self.room_cursor >= len(self.rooms):
            self.room_cursor = len(self.rooms) - 1

        if self.room_cursor < 0:
            self.room_cursor = 0

        if self.room_offset > self.room_cursor:
            self.room_offset = self.room_cursor

        self.mark_dirty()

    def move_room_cursor(self, delta, visible_count):
        if not self.rooms:
            return

        self.room_cursor += delta

        if self.room_cursor < 0:
            self.room_cursor = 0

        if self.room_cursor >= len(self.rooms):
            self.room_cursor = len(self.rooms) - 1

        if self.room_cursor < self.room_offset:
            self.room_offset = self.room_cursor

        max_offset = max(0, len(self.rooms) - visible_count)

        if self.room_cursor >= self.room_offset + visible_count:
            self.room_offset = self.room_cursor - visible_count + 1

        if self.room_offset > max_offset:
            self.room_offset = max_offset

        self.mark_dirty()

    def choose_current_room(self):
        if not self.rooms:
            return None

        self.selected_room = self.rooms[self.room_cursor]
        self.current_screen = "lights"
        self.mark_dirty()
        return self.selected_room
