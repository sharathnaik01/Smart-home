import paho.mqtt.client as mqtt
import json
import time
import ssl

ACCESS_TOKEN = 'FsMIRvzBSzv5lDt9exkJ'
THINGSBOARD_HOST = 'thingsboard.cloud'

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.tls_set(cert_reqs=ssl.CERT_NONE)  # For testing only, better to use valid certs in prod

client.connect(THINGSBOARD_HOST, 8883, 60)

while True:
    telemetry = {
        "temperature": 22.5,
        "humidity": 60,
        "light": "ON"
    }
    client.publish("v1/devices/me/telemetry", json.dumps(telemetry), 1)
    print("Published:", telemetry)
    time.sleep(5)
