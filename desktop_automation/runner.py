from .command_registry import COMMAND_REGISTRY


commands = [

    # VS Code Workflow

    "open_vscode",

    "create_folder",

    "create_file",

    "write_code",

    "save_file",

    "open_terminal",

    "run_file",

    "close_terminal",

    "close_vscode",

    # Task Manager Workflow

    "run_task_manager_workflow"
]


for command in commands:

    print()

    print(
        "=" * 50
    )

    print(
        f"Executing: {command}"
    )

    print(
        "=" * 50
    )

    try:

        COMMAND_REGISTRY[
            command
        ]()

        print(
            "Execution Success"
        )

    except Exception as error:

        print(
            f"Execution Failed: {error}"
        )