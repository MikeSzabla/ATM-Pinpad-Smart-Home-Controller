from umqtt.robust import MQTTClient
from app.config import CLIENT_ID
from app.infra.logger import info, error
import ujson

from secrets import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USER,
    MQTT_PASSWORD,
)

class MQTTManager():

    def __init__(self, state):
        self.client = MQTTClient(
            client_id=CLIENT_ID,
            server=MQTT_BROKER,
            port=MQTT_PORT,
            user=MQTT_USER or None,
            password=MQTT_PASSWORD or None,
            keepalive=60
        )
        self.state = state

    def connect(self):

        try:
            self.client.connect()
            info("Connected to MQTT broker.")
            return True

        except Exception as e:
            error(f"MQTT connection failed: {e}")
            return False

    def _callback(self, topic, msg):
        topic = topic.decode()
        device = topic.split("/")[-1]
        payload = ujson.loads(msg)
        self.state.devices[device] = payload

    def disconnect(self):
        self.client.disconnect()