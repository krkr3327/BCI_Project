# app/subscriber.py

import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}")
    print(f"Message: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("bci/test")

print("Waiting for messages...")

client.loop_forever()