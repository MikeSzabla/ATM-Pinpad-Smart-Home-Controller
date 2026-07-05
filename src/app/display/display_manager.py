from machine import Pin, SoftI2C

from app.config import I2C_SCL_GPIO, I2C_SDA_GPIO, OLED_WIDTH, OLED_HEIGHT
from app.infra.logger import info, error


class DisplayManager:

    def __init__(self, state):
        self.state = state
        self.display = None

        try:
            from lib.ssd1306 import SSD1306_I2C

            i2c = SoftI2C(scl=Pin(I2C_SCL_GPIO), sda=Pin(I2C_SDA_GPIO))
            self.display = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
            info("OLED display initialized.")

        except Exception as exc:
            error(f"Display unavailable: {exc}")

    def update(self):
        if not self.state.dirty:
            return

        if self.display is None:
            self.state.clear_dirty()
            return

        if self.state.current_screen == "rooms":
            self._draw_rooms_screen()

        elif self.state.current_screen == "lights":
            self._draw_lights_screen()

        else:
            self._draw_error_screen("Unknown screen")

        self.display.show()
        self.state.clear_dirty()

    def _draw_rooms_screen(self):
        self.display.fill(0)

        self._draw_centered("ROOMS", y=0)

        refresh_text = "[R]"
        refresh_x = OLED_WIDTH - (len(refresh_text) * 8)
        self.display.text(refresh_text, refresh_x, 0)

        if self.state.rooms_focus == "refresh":
            self.display.text("<", refresh_x - 8, 0)

        if not self.state.rooms:
            self.display.text("No rooms", 0, 20)
            self.display.text("Press Enter", 0, 30)
            return

        start = self.state.room_offset
        end = min(start + 4, len(self.state.rooms))
        y = 16

        for idx in range(start, end):
            room_name = self._room_to_name(self.state.rooms[idx])

            if idx == self.state.room_cursor and self.state.rooms_focus == "list":
                self.display.text(">", 0, y)
                self.display.text(room_name[:15], 8, y)
            elif idx == self.state.room_cursor:
                self.display.text("*", 0, y)
                self.display.text(room_name[:15], 8, y)
            else:
                self.display.text(" ", 0, y)
                self.display.text(room_name[:15], 8, y)

            y += 12

    def _draw_lights_screen(self):
        self.display.fill(0)
        self._draw_centered("LIGHTS", y=0)

        room_name = self._room_to_name(self.state.selected_room)
        self.display.text(room_name[:16], 0, 20)
        self.display.text("Cancel=Back", 0, 44)

    def _draw_error_screen(self, message):
        self.display.fill(0)
        self._draw_centered("ERROR", y=0)
        self.display.text(message[:16], 0, 20)

    def _draw_centered(self, text, y):
        x = max(0, (OLED_WIDTH - (len(text) * 8)) // 2)
        self.display.text(text, x, y)

    def _room_to_name(self, room):
        if isinstance(room, dict):
            return room.get("name", room.get("id", "(room)"))

        return str(room)
