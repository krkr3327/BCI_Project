import json
import time
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

commands = [
    "MOTOR_ON",
    "MOTOR_OFF",
    "MOTOR_FORWARD",
    "MOTOR_BACKWARD",
    "MOTOR_LEFT",
    "MOTOR_RIGHT",
    "MOTOR_STOP",
    "LED_ON",
    "LED_OFF",
    "LED_BLINK",
    "BUZZER_ON",
    "BUZZER_OFF",
    "SERVO_LEFT",
    "SERVO_RIGHT",
    "SERVO_CENTER"
]

for command in commands:

    payload = {
        "command": command
    }

    client.publish(
        "bci/embedded/commands",
        json.dumps(payload)
    )

    print(f"Published: {command}")

    time.sleep(2)

print("All Commands Published Successfully")