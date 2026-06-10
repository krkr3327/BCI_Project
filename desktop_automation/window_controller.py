import pyautogui
import time


class WindowController:

    @staticmethod
    def minimize_window():
        pyautogui.hotkey("win", "down")
        time.sleep(1)

    @staticmethod
    def maximize_window():
        pyautogui.hotkey("win", "up")
        time.sleep(1)

    @staticmethod
    def restore_window():
        pyautogui.hotkey("win", "up")
        time.sleep(1)

    @staticmethod
    def switch_window():
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)