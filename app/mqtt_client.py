import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

try:
    client.connect(broker, port, 60)

    print("MQTT Connected Successfully")

    client.publish(
        "bci/test",
        "Hello from Python Team"
    )

    print("Message Published Successfully")

except Exception as e:
    print("MQTT Error:", e)