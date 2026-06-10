from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from .desktop_detector import DesktopDetector
from .vscode_controller import VSCodeController
from .taskmanager_controller import TaskManagerController

app = Flask(__name__)

# Session and Logs
SESSIONS = []
LOGS = []

def log_action(action):
    LOGS.append(f"{datetime.now().strftime('%H:%M:%S')} - {action}")

@app.route("/")
def dashboard():
    running_apps = DesktopDetector.get_running_processes()
    return render_template(
        "dashboard.html",
        running_apps=running_apps,
        sessions=SESSIONS,
        logs=LOGS
    )

@app.route("/run_vscode")
def run_vscode():
    log_action("VS Code Workflow Started")
    VSCodeController.open_vscode()
    VSCodeController.create_folder()
    VSCodeController.create_file()
    VSCodeController.write_code()
    VSCodeController.save_file()
    VSCodeController.open_terminal()
    VSCodeController.run_file()
    VSCodeController.close_terminal()
    VSCodeController.close_tab()
    VSCodeController.close_vscode()
    log_action("VS Code Workflow Completed")
    SESSIONS.append({"workflow": "VS Code Workflow", "time": datetime.now().strftime("%H:%M:%S")})
    return redirect(url_for("dashboard"))

@app.route("/run_task_manager")
def run_task_manager():
    log_action("Task Manager Workflow Started")
    TaskManagerController.run_task_manager_workflow()
    log_action("Task Manager Workflow Completed")
    SESSIONS.append({"workflow": "Task Manager Workflow", "time": datetime.now().strftime("%H:%M:%S")})
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)