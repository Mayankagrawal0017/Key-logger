from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Listener, Key
def on_press(key):
    print(f"{key} pressed")

def on_release(key):
    if key == Key.esc:
         return

with Listener(on_press = on_press, on_release = on_release) as listener:
         listener.join()