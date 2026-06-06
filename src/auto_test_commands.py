import json
import time
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost",1883,60)

commands = [
    "MOTOR_ON",
    "MOTOR_FORWARD",
    "MOTOR_LEFT",
    "MOTOR_RIGHT",
    "MOTOR_BACKWARD",
    "LED_ON",
    "BUZZER_ON",
    "LED_OFF",
    "BUZZER_OFF",
    "MOTOR_OFF"
]

for cmd in commands:

    client.publish(
        "robotcar/commands",
        json.dumps({
            "command": cmd
        })
    )

    print(f"Sent: {cmd}")

    time.sleep(2)