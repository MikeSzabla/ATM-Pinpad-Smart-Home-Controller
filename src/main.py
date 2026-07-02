from wifi import WiFiManager
from mqtt_client import MQTTManager

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

import time

while True:
    time.sleep(1)