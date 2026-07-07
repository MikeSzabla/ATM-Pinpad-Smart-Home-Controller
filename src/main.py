from app.comms.wifi import WiFiManager
from app.comms.mqtt_client import MQTTManager
from app.input.keypad import Keypad
from app.input.input_simulator import SerialKeypadSimulator
from app.infra.logger import info, error
from app.config import MQTT_TOPIC_STATUS

import time

wifi = WiFiManager()

if not wifi.connect():
    error("WiFi connection failed")

mqtt = MQTTManager()

if not mqtt.connect():
    error("MQTT connection failed")

mqtt.publish_json(MQTT_TOPIC_STATUS, {"state": "online"}, retain=True)

info("Application started.")

keypad = Keypad()
simulator = SerialKeypadSimulator(keypad)

while True:

    simulator.update()
    mqtt.update()
    events = keypad.update()

    time.sleep_ms(20)