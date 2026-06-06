# BCI System - MQTT Integration & Command Routing

## Overview

This project implements MQTT-based communication between the Python Backend, Desktop Applications, IoT Devices, and Embedded Systems. The MQTT architecture enables reliable command delivery, status monitoring, telemetry collection, and alert management.

---

# Sprint 3 - Day 3

## Objective

Implement MQTT Integration and Command Routing to enable communication between different system components.

### Deliverables

* MQTT Topic Hierarchy Design
* MQTT Message Schema
* Command Routing Table
* MQTT Publish Testing
* End-to-End Pipeline Validation
* Latency Measurement

---

# MQTT Topic Hierarchy

## Desktop Topics

```text
bci/desktop/commands
bci/desktop/status
```

## IoT Topics

```text
bci/iot/commands
bci/iot/status
bci/iot/telemetry
```

## Embedded Topics

```text
bci/embedded/commands
bci/embedded/status
bci/embedded/telemetry
bci/embedded/alerts
```

---

# Embedded MQTT Topic Design

## Commands Topic

**Topic**

```text
bci/embedded/commands
```

**Purpose**

Used by the Python Backend to send control commands to ESP32-based Embedded Devices.

**Supported Commands**

```text
MOTOR_ON
MOTOR_OFF
MOTOR_FORWARD
MOTOR_BACKWARD
MOTOR_LEFT
MOTOR_RIGHT
MOTOR_STOP

LED_ON
LED_OFF
LED_BLINK

BUZZER_ON
BUZZER_OFF

SERVO_LEFT
SERVO_RIGHT
SERVO_CENTER

CAMERA_ON
CAMERA_OFF
```

### Example Command Message

```json
{
  "command": "MOTOR_FORWARD"
}
```

---

## Status Topic

**Topic**

```text
bci/embedded/status
```

**Purpose**

Publishes operational status of the embedded device.

### Example Status Message

```json
{
  "device_id": "ESP32_01",
  "status": "ONLINE"
}
```

---

## Telemetry Topic

**Topic**

```text
bci/embedded/telemetry
```

**Purpose**

Publishes real-time device and sensor information.

### Example Telemetry Message

```json
{
  "battery": 90,
  "speed": 20,
  "temperature": 29
}
```

---

## Alerts Topic

**Topic**

```text
bci/embedded/alerts
```

**Purpose**

Publishes warning and emergency notifications.

### Example Alert Message

```json
{
  "alert": "LOW_BATTERY"
}
```

---

# MQTT Message Schema

All MQTT messages follow the standard schema below.

```json
{
  "correlation_id": "uuid",
  "command": "MOTOR_FORWARD",
  "timestamp": "2025-06-05T10:00:00Z"
}
```

## Schema Fields

| Field          | Description                        |
| -------------- | ---------------------------------- |
| correlation_id | Unique identifier for traceability |
| command        | Requested action                   |
| timestamp      | Time of message creation           |

---

# Command Routing Table

| Command        | MQTT Topic            |
| -------------- | --------------------- |
| MOTOR_FORWARD  | bci/embedded/commands |
| MOTOR_BACKWARD | bci/embedded/commands |
| MOTOR_LEFT     | bci/embedded/commands |
| MOTOR_RIGHT    | bci/embedded/commands |
| MOTOR_STOP     | bci/embedded/commands |
| LED_ON         | bci/embedded/commands |
| LED_OFF        | bci/embedded/commands |
| BUZZER_ON      | bci/embedded/commands |
| BUZZER_OFF     | bci/embedded/commands |
| SERVO_LEFT     | bci/embedded/commands |
| SERVO_RIGHT    | bci/embedded/commands |

---

# End-to-End Communication Flow

```text
Brain Signals
      ↓
Machine Learning Model
      ↓
Python Backend
      ↓
MQTT Broker
      ↓
ESP32 Embedded Device
      ↓
Motor / LED / Buzzer / Servo
```

---

# Testing Topics

### Commands

```text
bci/embedded/commands
```

### Status

```text
bci/embedded/status
```

### Telemetry

```text
bci/embedded/telemetry
```

### Alerts

```text
bci/embedded/alerts
```

---

# Technologies Used

* Python
* FastAPI
* MQTT
* Mosquitto Broker
* Paho MQTT
* ESP32
* Git
* GitHub




# Author

**Ravi Kiran**

Task: Embedded MQTT Topic Hierarchy Design & README Update
