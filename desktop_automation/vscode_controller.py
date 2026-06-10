import os
import subprocess
import time
import pyautogui
import pyperclip


class VSCodeController:

    PROJECT_FOLDER = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "Sprint4_Demo"
    )

    FILE_NAME = "demo.py"

    @staticmethod
    def open_vscode():

        print("Opening VS Code...")

        os.makedirs(
            VSCodeController.PROJECT_FOLDER,
            exist_ok=True
        )

        subprocess.Popen([
            r"C:\Users\AB Lab 8\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            VSCodeController.PROJECT_FOLDER
        ])

        time.sleep(10)

        print("VS Code Opened")

    @staticmethod
    def create_folder():

        os.makedirs(
            VSCodeController.PROJECT_FOLDER,
            exist_ok=True
        )

        print(
            f"Folder Ready: "
            f"{VSCodeController.PROJECT_FOLDER}"
        )

        time.sleep(2)

    @staticmethod
    def create_file():

        print("Creating new file...")

        pyautogui.hotkey(
            "ctrl",
            "n"
        )

        time.sleep(3)

        print("New file created")

    @staticmethod
    def write_code():

        print("Writing code...")

        code = '''name = "Reddy"

print("Sprint 4 Day 3 Demo")

for i in range(1, 6):
    print("Count:", i)

print("Automation Completed")
'''

        pyperclip.copy(code)

        time.sleep(1)

        pyautogui.hotkey(
            "ctrl",
            "v"
        )

        time.sleep(2)

        print(
            "Code pasted successfully"
        )

    @staticmethod
    def save_file():

        print("Saving file...")

        pyautogui.hotkey(
            "ctrl",
            "s"
        )

        time.sleep(3)

        pyautogui.write(
            VSCodeController.FILE_NAME,
            interval=0.03
        )

        time.sleep(1)

        pyautogui.press(
            "enter"
        )

        time.sleep(3)

        print(
            f"Saved as "
            f"{VSCodeController.FILE_NAME}"
        )

    @staticmethod
    def open_terminal():

        print("Opening terminal...")

        pyautogui.hotkey(
            "ctrl",
            "`"
        )

        time.sleep(3)

        print(
            "Terminal Opened"
        )

    @staticmethod
    def run_file():

        print("Running Python File...")

        pyautogui.write(
            f"python {VSCodeController.FILE_NAME}",
            interval=0.03
        )

        pyautogui.press(
            "enter"
        )

        time.sleep(5)

        print(
            "Python File Executed"
        )

    @staticmethod
    def close_terminal():

        print(
            "Closing Terminal..."
        )

        pyautogui.hotkey(
            "ctrl",
            "`"
        )

        time.sleep(2)

        print(
            "Terminal Closed"
        )

    @staticmethod
    def close_tab():

        print(
            "Closing Current Tab..."
        )

        pyautogui.hotkey(
            "ctrl",
            "w"
        )

        time.sleep(2)

        print(
            "Tab Closed"
        )

    @staticmethod
    def close_vscode():

        print(
            "Closing VS Code..."
        )

        pyautogui.hotkey(
            "alt",
            "f4"
        )

        time.sleep(3)

        print(
            "VS Code Closed"
        )