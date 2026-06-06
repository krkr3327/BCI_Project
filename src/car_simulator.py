import json
import time
import paho.mqtt.client as mqtt

car_state = {
    "motor": "OFF",
    "direction": "STOP",
    "led": "OFF",
    "buzzer": "OFF",
    "battery": 100
}

def publish_status(client):
    client.publish(
        "robotcar/status",
        json.dumps({
            "motor": car_state["motor"],
            "direction": car_state["direction"],
            "led": car_state["led"],
            "buzzer": car_state["buzzer"]
        })
    )

def publish_telemetry(client):
    client.publish(
        "robotcar/telemetry",
        json.dumps({
            "battery": car_state["battery"],
            "speed": 20 if car_state["motor"] == "ON" else 0
        })
    )

def publish_alert(client, alert):
    client.publish(
        "robotcar/alerts",
        json.dumps({
            "alert": alert
        })
    )

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())
    command = data["command"]

    print(f"\nCommand Received: {command}")

    if command == "MOTOR_ON":
        car_state["motor"] = "ON"
        print("🚗 Motor Started")

    elif command == "MOTOR_OFF":
        car_state["motor"] = "OFF"
        print("🛑 Motor Stopped")

    elif command == "MOTOR_FORWARD":
        car_state["direction"] = "FORWARD"
        print("⬆ Moving Forward")

    elif command == "MOTOR_BACKWARD":
        car_state["direction"] = "BACKWARD"
        print("⬇ Moving Backward")

    elif command == "MOTOR_LEFT":
        car_state["direction"] = "LEFT"
        print("⬅ Turning Left")

    elif command == "MOTOR_RIGHT":
        car_state["direction"] = "RIGHT"
        print("➡ Turning Right")

    elif command == "LED_ON":
        car_state["led"] = "ON"
        print("💡 LED ON")

    elif command == "LED_OFF":
        car_state["led"] = "OFF"
        print("💡 LED OFF")

    elif command == "BUZZER_ON":
        car_state["buzzer"] = "ON"
        print("🔊 Buzzer ON")

    elif command == "BUZZER_OFF":
        car_state["buzzer"] = "OFF"
        print("🔇 Buzzer OFF")

    publish_status(client)
    publish_telemetry(client)

    if car_state["battery"] < 20:
        publish_alert(client, "LOW_BATTERY")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("robotcar/commands")

print("🚗 Smart Robot Car Started")

client.loop_forever()