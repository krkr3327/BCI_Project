import pyautogui
import time


class KeyboardController:

    @staticmethod
    def copy():
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)

    @staticmethod
    def paste():
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

    @staticmethod
    def save():
        pyautogui.hotkey("ctrl", "s")
        time.sleep(1)

    @staticmethod
    def undo():
        pyautogui.hotkey("ctrl", "z")
        time.sleep(1)

    @staticmethod
    def redo():
        pyautogui.hotkey("ctrl", "y")
        time.sleep(1)

    @staticmethod
    def select_all():
        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)

    @staticmethod
    def alt_tab():
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)