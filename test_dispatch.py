from src.command_dispatcher import dispatch_command

test_commands = [
    "PLAY",
    "VOLUME_UP",
    "VOLUME_DOWN",
    "OPEN_BROWSER",
    "SCROLL_UP",
    "SCROLL_DOWN"
]

print("Starting Integration Test...")

for cmd in test_commands:
    print(f"Testing: {cmd}")
    dispatch_command(cmd)

print("Integration Test Completed")