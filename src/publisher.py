import json
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

message = {
    "command": "MOTOR_ON"
}

client.publish(
    "bci/embedded/commands",
    json.dumps(message)
)

print("Message Published")