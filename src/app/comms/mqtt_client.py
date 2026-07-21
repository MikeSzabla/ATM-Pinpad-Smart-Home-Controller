from umqtt.robust import MQTTClient
from app.config import CLIENT_ID
from app.infra.logger import info, error

from secrets import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USER,
    MQTT_PASSWORD,
)

class MQTTManager:

    def __init__(self):
        self.client = MQTTClient(
            client_id=CLIENT_ID,
            server=MQTT_BROKER,
            port=MQTT_PORT,
            user=MQTT_USER or None,
            password=MQTT_PASSWORD or None,
            keepalive=60
        )

    def connect(self):

        try:
            self.client.connect()
            info("Connected to MQTT broker.")
            return True

        except Exception as e:
            error(f"MQTT connection failed: {e}")
            return False

    def publish(self, topic, payload, retain=False):
        pass

    def disconnect(self):
        self.client.disconnect()