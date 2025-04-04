import pyperclip
import time

clipboard_history = []

print("Clipboard Manager started. Press Ctrl+C to stop.")

try:
    recent_value = ""

    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            clipboard_history.append(recent_value)
            print(f"Copied: {recent_value}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nClipboard Manager stopped.")
    print("\nClipboard History:")
    for i, item in enumerate(clipboard_history, 1):
        print(f"{i}: {item}")

    