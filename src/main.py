from app.comms.wifi import WiFiManager
from app.comms.mqtt_client import MQTTManager
from app.input.keypad import Keypad
from app.input.input_simulator import SerialKeypadSimulator
from app.state import ApplicationState
from app.ui.ui_manager import UIManager
from app.display.display_manager import DisplayManager
from app.infra.logger import info, error
from app.config import MQTT_TOPIC_STATUS

import time

wifi = WiFiManager()

if not wifi.connect():
    error("WiFi connection failed")

state = ApplicationState()


def _on_rooms_update(rooms):
    state.set_rooms(rooms)


mqtt = MQTTManager(on_rooms_update=_on_rooms_update)

if not mqtt.connect():
    error("MQTT connection failed")

mqtt.publish_json(MQTT_TOPIC_STATUS, {"state": "online"}, retain=True)

info("Application started.")

keypad = Keypad()
simulator = SerialKeypadSimulator(keypad)
ui = UIManager(state, mqtt)
display = DisplayManager(state)

while True:

    simulator.update()

    mqtt.update()

    events = keypad.update()
    ui.update(events)
    display.update()

    if not wifi.is_connected():
        state.last_error = "WiFi disconnected"

    time.sleep_ms(20)