from .vscode_controller import VSCodeController
from .taskmanager_controller import TaskManagerController

COMMAND_REGISTRY = {

    # VS Code Commands

    "open_vscode":
        VSCodeController.open_vscode,

    "create_folder":
        VSCodeController.create_folder,

    "create_file":
        VSCodeController.create_file,

    "write_code":
        VSCodeController.write_code,

    "save_file":
        VSCodeController.save_file,

    "open_terminal":
        VSCodeController.open_terminal,

    "run_file":
        VSCodeController.run_file,

    "close_terminal":
        VSCodeController.close_terminal,

    "close_vscode":
        VSCodeController.close_vscode,

    # Task Manager Workflow

    "run_task_manager_workflow":
        TaskManagerController.run_task_manager_workflow
}