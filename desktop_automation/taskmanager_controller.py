import os
import time
import pyautogui
import pygetwindow as gw


class TaskManagerController:

    @staticmethod
    def open_task_manager():

        print("\n[EXECUTING] OPEN_TASK_MANAGER")

        os.system(
            'powershell -Command "Start-Process taskmgr -Verb runAs"'
        )

        time.sleep(5)

        print(
            "[SUCCESS] TASK_MANAGER_OPENED"
        )

    @staticmethod
    def maximize_task_manager():

        print(
            "\n[EXECUTING] MAXIMIZE_TASK_MANAGER"
        )

        windows = gw.getWindowsWithTitle(
            "Task Manager"
        )

        if windows:

            windows[0].maximize()

            time.sleep(2)

        print(
            "[SUCCESS] TASK_MANAGER_MAXIMIZED"
        )

    @staticmethod
    def open_demo_notepad():

        print(
            "\n[EXECUTING] OPEN_DEMO_NOTEPAD"
        )

        os.system(
            "start notepad"
        )

        time.sleep(3)

        pyautogui.write(
            "Sprint 4 Desktop Automation Demo",
            interval=0.05
        )

        time.sleep(2)

        print(
            "[SUCCESS] DEMO_NOTEPAD_OPENED"
        )

    @staticmethod
    def focus_task_manager():

        windows = gw.getWindowsWithTitle(
            "Task Manager"
        )

        if windows:

            windows[0].activate()

            time.sleep(2)

    @staticmethod
    def open_performance_tab():

        print(
            "\n[EXECUTING] OPEN_PERFORMANCE_TAB"
        )

        pyautogui.click(
            95,
            58
        )

        time.sleep(2)

        print(
            "[SUCCESS] PERFORMANCE_TAB_OPENED"
        )

    @staticmethod
    def open_app_history():

        print(
            "\n[EXECUTING] OPEN_APP_HISTORY"
        )

        pyautogui.click(
            95,
            260
        )

        time.sleep(2)

    @staticmethod
    def open_startup_apps():

        print(
            "\n[EXECUTING] OPEN_STARTUP_APPS"
        )

        pyautogui.click(
            95,
            300
        )

        time.sleep(2)

    @staticmethod
    def open_users():

        print(
            "\n[EXECUTING] OPEN_USERS"
        )

        pyautogui.click(
            95,
            340
        )

        time.sleep(2)

    @staticmethod
    def open_details():

        print(
            "\n[EXECUTING] OPEN_DETAILS"
        )

        pyautogui.click(
            95,
            380
        )

        time.sleep(2)

    @staticmethod
    def open_services():

        print(
            "\n[EXECUTING] OPEN_SERVICES"
        )

        pyautogui.click(
            95,
            420
        )

        time.sleep(2)

    @staticmethod
    def open_processes_tab():

        print(
            "\n[EXECUTING] OPEN_PROCESSES_TAB"
        )

        pyautogui.click(
            30,
            58
        )

        time.sleep(2)

        print(
            "[SUCCESS] PROCESSES_TAB_OPENED"
        )

    @staticmethod
    def terminate_demo_notepad():

        print(
            "\n[EXECUTING] TERMINATE_NOTEPAD"
        )

        os.system(
            "taskkill /f /im notepad.exe"
        )

        time.sleep(2)

        print(
            "[SUCCESS] NOTEPAD_TERMINATED"
        )

    @staticmethod
    def close_task_manager():

        print(
            "\n[EXECUTING] CLOSE_TASK_MANAGER"
        )

        TaskManagerController.focus_task_manager()

        pyautogui.hotkey(
            "alt",
            "f4"
        )

        time.sleep(2)

        print(
            "[SUCCESS] TASK_MANAGER_CLOSED"
        )

    @staticmethod
    def run_task_manager_workflow():

        TaskManagerController.open_task_manager()

        TaskManagerController.maximize_task_manager()

        TaskManagerController.open_demo_notepad()

        TaskManagerController.focus_task_manager()

        TaskManagerController.open_performance_tab()

        TaskManagerController.open_app_history()

        TaskManagerController.open_startup_apps()

        TaskManagerController.open_users()

        TaskManagerController.open_details()

        TaskManagerController.open_services()

        TaskManagerController.open_processes_tab()

        TaskManagerController.terminate_demo_notepad()

        TaskManagerController.close_task_manager()