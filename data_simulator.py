import time
import random
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect

try:
    print("Connecting to MQTT broker...")
    client.connect("localhost", 1883, 60)
    client.loop_start()

    while True:
        heart_rate = random.randint(60, 100)
        sys = random.randint(100, 140)
        dia = random.randint(60, 90)
        data = {"hr": heart_rate, "sys": sys, "dia": dia}
        client.publish("vitals", json.dumps(data))
        print("Sent:", data)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping data simulator...")
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
    client.loop_stop()
    client.disconnect()