from app.comms.wifi import WiFiManager
from app.comms.MQTTManager import MQTTManager
from app.comms.DeviceState import DeviceState
from app.input.keypad import Keypad
from app.input.input_simulator import SerialKeypadSimulator
from app.ui.ScreenManager import ScreenManager
from app.ui.Screens.RoomSelect import RoomSelectScreen
from app.infra.logger import info, error
from app.config import MQTT_TOPIC_STATUS

import time

# Initialize screen manager for UI navigation
sm = ScreenManager()

# Connect to WiFi
wifi = WiFiManager()
if not wifi.connect():
    error("WiFi connection failed")

# Connect to MQTT broker
ds = DeviceState()
mqtt = MQTTManager(ds)
if not mqtt.connect():
    error("MQTT connection failed")

info("Application started.")

# Initialize input handling
keypad = Keypad()
simulator = SerialKeypadSimulator(keypad)

# Load initial screen
sm.switch_to(RoomSelectScreen)

# Main event loop
while True:
    # Poll for new keypad inputs
    simulator.update()
    events = keypad.update()
    mqtt.client.check_msg()

    # Route keypad events to active screen
    for key in events:
        sm.handle_keypad_event(key)

    time.sleep_ms(20)