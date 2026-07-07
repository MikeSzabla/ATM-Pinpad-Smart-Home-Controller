CLIENT_ID = "atm_pinpad"

MQTT_TOPIC_STATUS = "atm_pinpad/status"
MQTT_TOPIC_REQUEST = "atm_pinpad/cmd/request"
MQTT_TOPIC_STATE_ROOMS = "atm_pinpad/state/rooms"
MQTT_QOS = 1

WIFI_TIMEOUT_SECONDS = 15
MQTT_TIMEOUT_SECONDS = 5

BUTTON_MINUS_GPIO = 4

BUTTONS = {
    "minus": BUTTON_MINUS_GPIO,
}

# Virtual input support lets UI logic be tested before all hardware keys are wired.
SIMULATION_ENABLED = True

VALID_BUTTON_NAMES = (
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "clear",
    "cancel",
    "enter",
    "plus",
    "minus",
    "blank",
)
