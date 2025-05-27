import json
import requests
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe("vitals")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("Received data:", data)
        res = requests.post("http://localhost:5000/predict", json=data)
        if res.status_code == 200:
            prediction = res.json()
            print("Predicción:", prediction)
        else:
            print("Error:", res.status_code, res.text)
    except Exception as e:
        print("Error processing message:", str(e))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    print("Connecting to MQTT broker...")
    client.connect("localhost", 1883, 60)
    print("Waiting for messages...")
    client.loop_forever()
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")