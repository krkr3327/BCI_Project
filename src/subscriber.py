import paho.mqtt.client as mqtt

print("Step 1: Import Successful")

def on_message(client, userdata, msg):
    print("\nReceived Message")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())

print("Step 2: Creating Client")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

print("Step 3: Connecting Broker")

client.connect("localhost", 1883, 60)

print("Step 4: Connected")

client.on_message = on_message

client.subscribe("bci/embedded/#")

print("Step 5: Subscribed")

print("Listening for MQTT messages...")

client.loop_forever()