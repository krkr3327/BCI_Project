from src.browser_control import (
    open_browser,
    open_youtube,
    open_github
)

print("Opening Google...")
open_browser()

input("Press Enter to open YouTube...")

print("Opening YouTube...")
open_youtube()

input("Press Enter to open GitHub...")

print("Opening GitHub...")
open_github()

print("Browser Automation Test Completed")