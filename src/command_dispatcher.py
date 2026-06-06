from src.media_control import (
    play_pause,
    volume_up,
    volume_down
)

from src.browser_control import (
    open_browser,
    open_youtube,
    open_github
)

from src.app_control import (
    open_notepad,
    open_calculator,
    open_paint
)

from src.scroll_control import (
    scroll_up,
    scroll_down
)


def dispatch_command(command):

    print(f"Received Command: {command}")

    if command == "PLAY":
        print("Executing PLAY")
        play_pause()

    elif command == "PAUSE":
        print("Executing PAUSE")
        play_pause()

    elif command == "VOLUME_UP":
        print("Executing VOLUME_UP")
        volume_up()

    elif command == "VOLUME_DOWN":
        print("Executing VOLUME_DOWN")
        volume_down()

    elif command == "OPEN_BROWSER":
        print("Executing OPEN_BROWSER")
        open_browser()

    elif command == "OPEN_YOUTUBE":
        print("Executing OPEN_YOUTUBE")
        open_youtube()

    elif command == "OPEN_GITHUB":
        print("Executing OPEN_GITHUB")
        open_github()

    elif command == "OPEN_NOTEPAD":
        print("Executing OPEN_NOTEPAD")
        open_notepad()

    elif command == "OPEN_CALCULATOR":
        print("Executing OPEN_CALCULATOR")
        open_calculator()

    elif command == "OPEN_PAINT":
        print("Executing OPEN_PAINT")
        open_paint()

    elif command == "SCROLL_UP":
        print("Executing SCROLL_UP")
        scroll_up()

    elif command == "SCROLL_DOWN":
        print("Executing SCROLL_DOWN")
        scroll_down()

    else:
        print(f"Unknown Command: {command}")