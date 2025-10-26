import random
import webbrowser
from threading import Timer
from pynput import keyboard
import os
import sys
import shutil
import ctypes

try:
    import winshell
except Exception:
    winshell = None

HWND_BROADCAST = 0xFFFF
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a

def subir_volumen_paso():
    """Sube el volumen 2% (un paso)."""
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP << 16)

class KBTroller:
    """
    Troller simple que abre una URL cuando se pulsa una letra aleatoria.
    Parámetros:
      url: str - URL a abrir (si vacía no abre nada)
      vol: bool - si True intenta subir el volumen (Windows)
      persistence: bool - si True intenta copiar el ejecutable al Startup (Windows)
      debug: bool - si True imprime mensajes de depuración
    """

    def __init__(self, url: str = "", vol: bool = False, persistence: bool = False, debug: bool = True):
        self.url = url
        self.vol = bool(vol)
        self.persistence = bool(persistence)
        self.debug = bool(debug)
        self.kb = list("abcdefghijklmnñopqrstuvwxyz")
        self.letter = self.get_letter()
        self._debounce = False  

    def get_letter(self):
        letter = random.choice(self.kb)
        if self.debug:
            print(f"[DEBUG] Nueva letra objetivo: {letter}")
        return letter

    def open_url(self):
        if not self.url:
            if self.debug:
                print("[DEBUG] URL vacía: no se abrirá nada.")
            return
        webbrowser.open(self.url, new=2)
        if self.debug:
            print(f"[DEBUG] Abriendo URL: {self.url}")

    def _reset_debounce(self):
        self._debounce = False

    def _on_press(self, key):
        try:
            char = key.char.lower()
        except AttributeError:
            return 

        if self.debug:
            print(f"[DEBUG] Tecla pulsada: {char}")

        if char == self.letter and not self._debounce:
            if self.debug:
                print(f"[DEBUG] Letra correcta '{char}'. Ejecutando acciones.")
            if self.vol:
                self.set_volume_max()

            self.open_url()
            self.letter = self.get_letter()

            self._debounce = True
            Timer(1.0, self._reset_debounce).start()

    def on_release(self, key):
        pass

    def set_volume_max(self):
        """
        Sube el volumen usando ctypes. Cada llamada sube un paso (~2%).
        Para aumentar más, puedes llamar varias veces.
        """
        try:
            for _ in range(10): 
                subir_volumen_paso()
            if self.debug:
                print("[DEBUG] Volumen subido varios pasos.")
            return True
        except Exception as e:
            if self.debug:
                print(f"[DEBUG] Error subiendo volumen: {e}")
            return False

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
        if self.persistence:
            if self.debug:
                print("[DEBUG] persistence=True -> intentando añadir a Startup")
            self.add_to_startup()

        if self.debug:
            print(f"[DEBUG] Escuchando... pulsa la letra '{self.letter}' (Vol={'ON' if self.vol else 'OFF'}, Persistence={'ON' if self.persistence else 'OFF'})")
        else:
            print(f"Escuchando... pulsa la letra '{self.letter}'")

        with keyboard.Listener(on_press=self._on_press, on_release=self.on_release) as listener:
            listener.join()


kb = KBTroller(url="https://ia801502.us.archive.org/27/items/y-2-mate.is-rick-astley-never-gonna-give-you-up-remastered-4-k-60fps-ai-o-ybdtq-/Y2Mate.is%20-%20Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20%28Remastered%204K%2060fps%2CAI%29-o-YBDTqX_ZU-1080p-1658021729392.mp4", vol=True, persistence=False, debug=False)
kb.run()
