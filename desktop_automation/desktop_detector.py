import psutil
import pygetwindow as gw


class DesktopDetector:

    @staticmethod
    def get_running_processes():

        processes = []

        for process in psutil.process_iter():

            try:
                processes.append(
                    process.name()
                )

            except Exception:
                pass

        return processes

    @staticmethod
    def get_active_window():

        return gw.getActiveWindowTitle()

    @staticmethod
    def get_all_windows():

        return gw.getAllTitles()

    @staticmethod
    def is_window_visible(title):

        windows = gw.getWindowsWithTitle(
            title
        )

        return len(windows) > 0