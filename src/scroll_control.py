import pyautogui

pyautogui.FAILSAFE = True

def scroll_up():
    pyautogui.scroll(500)

def scroll_down():
    pyautogui.scroll(-500)