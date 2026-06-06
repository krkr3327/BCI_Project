import pandas as pd
import numpy as np
import webbrowser
import pyautogui
import time

# Dataset path
file_path = r"C:\Users\AB Lab 8\Desktop\sprint 3 project2\BCI_Project\data\user_c.csv"

# Read dataset
df = pd.read_csv(file_path)S

print("Dataset Loaded Successfully")
print(df.shape)

# Keep only numeric EEG columns
numeric_df = df.select_dtypes(include=[np.number])

# Open YouTube
webbrowser.open("https://www.youtube.com")
time.sleep(5)

# Maximum signal value in dataset
max_signal = numeric_df.abs().max().max()

for index, row in numeric_df.iterrows():

    # Generate confidence automatically from EEG values
    signal_strength = row.abs().mean()

    confidence = signal_strength / max_signal

    print(f"\nRow: {index}")
    print(f"Confidence: {confidence:.3f}")

    if confidence >= 0.95:

        print("SEARCH_MUSIC")

        webbrowser.open(
            "https://www.youtube.com/results?search_query=latest+music"
        )

    elif confidence >= 0.90:

        print("SEARCH_AI")

        webbrowser.open(
            "https://www.youtube.com/results?search_query=artificial+intelligence"
        )

    elif confidence >= 0.85:

        print("SEARCH_NEWS")

        webbrowser.open(
            "https://www.youtube.com/results?search_query=breaking+news"
        )

    elif confidence >= 0.80:

        print("SEARCH_PYTHON")

        webbrowser.open(
            "https://www.youtube.com/results?search_query=python+tutorial"
        )

    elif confidence >= 0.75:

        print("NEXT_VIDEO")

        pyautogui.hotkey("shift", "n")

    elif confidence >= 0.70:

        print("PREVIOUS_VIDEO")

        pyautogui.hotkey("shift", "p")

    elif confidence >= 0.65:

        print("VOLUME_UP")

        pyautogui.press("up")

    elif confidence >= 0.60:

        print("VOLUME_DOWN")

        pyautogui.press("down")

    elif confidence >= 0.55:

        print("SCROLL_DOWN")

        pyautogui.scroll(-500)

    elif confidence >= 0.50:

        print("SCROLL_UP")

        pyautogui.scroll(500)

    elif confidence >= 0.45:

        print("PLAY / PAUSE")

        pyautogui.press("space")

    else:

        print("LOW CONFIDENCE - SKIPPED")

    time.sleep(2)

print("\nAutomation Completed")