import keyboard


def play_pause():
    keyboard.send("play/pause media")


def volume_up():
    keyboard.send("volume up")


def volume_down():
    keyboard.send("volume down")