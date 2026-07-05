from umqtt.robust import MQTTClient

try:
    import ujson as json
except ImportError:
    import json

from secrets import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USER,
    MQTT_PASSWORD,
)

from app.config import (
    CLIENT_ID,
    MQTT_QOS,
    MQTT_TOPIC_REQUEST,
    MQTT_TOPIC_STATE_ROOMS,
)

from app.infra.logger import info, error


class MQTTManager:

    def __init__(self, on_rooms_update=None):
        self.on_rooms_update = on_rooms_update

        self.client = MQTTClient(
            client_id=CLIENT_ID,
            server=MQTT_BROKER,
            port=MQTT_PORT,
            user=MQTT_USER or None,
            password=MQTT_PASSWORD or None,
            keepalive=60,
        )

        self.client.set_callback(self._on_message)

    def connect(self):
        try:
            self.client.connect()
            self.client.subscribe(MQTT_TOPIC_STATE_ROOMS.encode(), qos=MQTT_QOS)
            info("Connected to MQTT broker.")
            return True

        except Exception as exc:
            error(f"MQTT connection failed: {exc}")
            return False

    def publish(self, topic, payload, retain=False):
        self.client.publish(
            topic.encode(),
            payload.encode(),
            retain=retain,
            qos=MQTT_QOS,
        )

    def publish_json(self, topic, payload, retain=False):
        self.publish(topic, json.dumps(payload), retain=retain)

    def request_rooms(self):
        self.publish_json(
            MQTT_TOPIC_REQUEST,
            {"type": "rooms"},
            retain=False,
        )

    def update(self):
        try:
            self.client.check_msg()
        except Exception as exc:
            error(f"MQTT update error: {exc}")

    def _on_message(self, topic, payload):
        try:
            topic_text = topic.decode() if isinstance(topic, bytes) else str(topic)
            payload_text = payload.decode() if isinstance(payload, bytes) else str(payload)

            if topic_text != MQTT_TOPIC_STATE_ROOMS:
                return

            message = json.loads(payload_text)
            rooms = message.get("rooms", [])

            if self.on_rooms_update is not None:
                self.on_rooms_update(rooms)

            info(f"Rooms snapshot received with {len(rooms)} entries.")

        except Exception as exc:
            error(f"Failed to process MQTT message: {exc}")

    def disconnect(self):
        self.client.disconnect()
