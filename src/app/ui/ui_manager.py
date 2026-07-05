from app.config import ROOM_SCROLL_STEP
from app.infra.logger import info


class UIManager:

    def __init__(self, state, mqtt):
        self.state = state
        self.mqtt = mqtt

    def update(self, events):
        if self.state.current_screen == "rooms":
            self._update_rooms(events)
            return

        if self.state.current_screen == "lights":
            self._update_lights(events)

    def _update_rooms(self, events):
        if self.state.request_rooms_pending:
            self.mqtt.request_rooms()
            self.state.request_rooms_pending = False
            self.state.mark_dirty()

        for button in events:
            self._handle_rooms_button(button)

    def _update_lights(self, events):
        for button in events:
            if button == "cancel":
                self.state.current_screen = "rooms"
                self.state.mark_dirty()
                return

            if button == "enter":
                room = self.state.selected_room or "(unknown)"
                info(f"Lights screen enter pressed for room: {room}")

    def _handle_rooms_button(self, button):
        if button == "blank":
            return

        if button == "4":
            self.state.rooms_focus = "list"
            self.state.mark_dirty()
            return

        if button == "6":
            self.state.rooms_focus = "refresh"
            self.state.mark_dirty()
            return

        if button == "2" and self.state.rooms_focus == "list":
            self.state.move_room_cursor(-ROOM_SCROLL_STEP, visible_count=4)
            return

        if button == "8" and self.state.rooms_focus == "list":
            self.state.move_room_cursor(ROOM_SCROLL_STEP, visible_count=4)
            return

        if button == "enter":
            if self.state.rooms_focus == "refresh":
                info("Room refresh requested from UI.")
                self.state.request_rooms_pending = True
                self.state.mark_dirty()
                return

            selected = self.state.choose_current_room()
            if selected is not None:
                info(f"Selected room: {selected}")
