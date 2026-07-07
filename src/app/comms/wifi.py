import network
import time

from app.infra.logger import info, error
from secrets import WIFI_SSID, WIFI_PASSWORD
from app.config import WIFI_TIMEOUT_SECONDS


class WiFiManager:

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        info("Starting Wi-Fi connection process.")
        self.wlan.active(True)

        if self.wlan.isconnected():
            info("Connection already established.")
            return True

        info(f"Connecting to {WIFI_SSID}...")

        self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        timeout = WIFI_TIMEOUT_SECONDS

        while timeout > 0:
            if self.wlan.isconnected():
                info("WiFi connected.")
                info(f"IP: {self.wlan.ifconfig()[0]}")
                return True

            time.sleep(1)
            timeout -= 1

        error("Failed to connect to WiFi.")
        return False

    def is_connected(self):
        return self.wlan.isconnected()

    def ip_address(self):
        if self.wlan.isconnected():
            return self.wlan.ifconfig()[0]
        return None
