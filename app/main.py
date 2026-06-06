@app.post("/receive-command")
def receive_command(data: CommandRequest):

    print("DEBUG: NEW CODE RUNNING")

    if data.confidence < 0.70:
        return {
            "status": "rejected",
            "reason": "Confidence below threshold",
            "confidence": data.confidence
        }

    return {
        "status": "received",
        "command": data.command,
        "confidence": data.confidence
    }