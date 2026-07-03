from wifi import WiFiManager
from mqtt_client import MQTTManager
from keypad import Keypad

import time

wifi = WiFiManager()

if not wifi.connect():
    raise RuntimeError("WiFi connection failed")

mqtt = MQTTManager()

if not mqtt.connect():
    raise RuntimeError("MQTT connection failed")

mqtt.publish(
    "atm_pinpad/status",
    "online",
    retain=True
)

print("Application started.")

keypad = Keypad()

while True:

    for button in keypad.update():
        print(f"keypad.update() called from main: on Button {button}")
        mqtt.publish("atm_pinpad/button", button)

    time.sleep_ms(20)