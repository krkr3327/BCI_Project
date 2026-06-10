import pyautogui
import time


class MouseController:

    @staticmethod
    def left_click():
        pyautogui.click()

    @staticmethod
    def right_click():
        pyautogui.rightClick()

    @staticmethod
    def double_click():
        pyautogui.doubleClick()

    @staticmethod
    def drag_and_drop():
        pyautogui.dragRel(
            200,
            0,
            duration=1
        )

    @staticmethod
    def scroll_up():
        pyautogui.scroll(500)

    @staticmethod
    def scroll_down():
        pyautogui.scroll(-500)