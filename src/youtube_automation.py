import webbrowser
import pyautogui
import time


# Open YouTube Home Page
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    time.sleep(5)


# Open Python Tutorial Video
def open_python_video():
    webbrowser.open(
        "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
    )
    time.sleep(5)


# Scroll Down
def scroll_down():
    pyautogui.scroll(-500)


# Scroll Up
def scroll_up():
    pyautogui.scroll(500)


# Volume Up
def volume_up():
    pyautogui.press("up")


# Volume Down
def volume_down():
    pyautogui.press("down")


# Pause Video
def pause_video():
    pyautogui.press("space")


# Play Video
def play_video():
    pyautogui.press("space")


# Full Demo
def youtube_demo():

    print("Opening YouTube...")
    open_youtube()

    print("Opening Python Tutorial Video...")
    open_python_video()

    time.sleep(5)

    print("Volume Up...")
    volume_up()

    time.sleep(2)

    print("Volume Down...")
    volume_down()

    time.sleep(2)

    print("Scroll Down...")
    scroll_down()

    time.sleep(2)

    print("Scroll Up...")
    scroll_up()

    time.sleep(2)

    print("Pause Video...")
    pause_video()

    time.sleep(3)

    print("Play Video...")
    play_video()

    print("Demo Completed")