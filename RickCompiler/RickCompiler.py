# By sug023
# THIS SCRIPT HAS BEEN CREATED FOR INFORMATIONAL AND EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY CONSEQUENCES. USE IT AT YOUR OWN RISK.

import os
import subprocess
import ast
from glob import glob
import sys

# Initialize color support for terminal output or install it if missing
try:
    import colorama
    colorama.init(autoreset=True)
except ImportError:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "colorama"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    import colorama
    colorama.init(autoreset=True)

BANNER = r'''
 ________  ___  ________  ___  __    ________  ___  ___       _______   ________     
|\   __  \|\  \|\   ____\|\  \|\  \ |\   __  \|\  \|\  \     |\  ___ \ |\   __  \    
\ \  \|\  \ \  \ \  \___|\ \  \/  /|\ \  \|\  \ \  \ \  \    \ \   __/|\ \  \|\  \   
 \ \   _  _\ \  \ \  \    \ \   ___  \ \   ____\ \  \ \  \    \ \  \_|/_\ \   _  _\  
  \ \  \\  \\ \  \ \  \____\ \  \\ \  \ \  \___|\ \  \ \  \____\ \  \_|\ \ \  \\  \| 
   \ \__\\ _\\ \__\ \_______\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|__|\|__|\|__|\|_______|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|\|__|
'''


def print_gradient_banner(text):
    """Print a colored ASCII banner with a smooth RGB gradient."""
    lines = text.splitlines()
    start_color = (255, 0, 0)       # Red
    end_color = (128, 0, 128)       # Purple
    for line in lines:
        line_len = len(line)
        for i, char in enumerate(line):
            r = int(start_color[0] + (end_color[0] - start_color[0]) * i / max(1, line_len - 1))
            g = int(start_color[1] + (end_color[1] - start_color[1]) * i / max(1, line_len - 1))
            b = int(start_color[2] + (end_color[2] - start_color[2]) * i / max(1, line_len - 1))
            print(f"\033[38;2;{r};{g};{b}m{char}", end="")
        print("\033[0m")


class PythonToExeCompiler:
    def __init__(self, directory=None):
        """Initialize the compiler and set the working directory."""
        self.directory = directory or os.path.dirname(os.path.abspath(__file__))

    def get_imports(self, script_path):
        """Parse the target script to extract all imported modules using AST."""
        with open(script_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=script_path)
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])
        return imports

    def ensure_packages_installed(self, packages):
        """Check and install any missing packages using pip."""
        for pkg in packages:
            try:
                __import__(pkg)
            except ImportError:
                print(f"\033[33m[*] Package '{pkg}' not found. Installing...\033[0m")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", pkg],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

    def compile_script(self, script_path):
        """Compile the selected Python script into an executable using PyInstaller."""
        imports = self.get_imports(script_path)
        std_libs = sys.builtin_module_names
        external_packages = [pkg for pkg in imports if pkg not in std_libs]

        if external_packages:
            self.ensure_packages_installed(external_packages)

        # Ensure PyInstaller is installed
        try:
            import PyInstaller
        except ImportError:
            print("\033[33m[*] PyInstaller not found. Installing...\033[0m")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "pyinstaller"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        # Run PyInstaller to generate executable
        print(f"\033[35m[*] Compiling '{os.path.basename(script_path)}'...\033[0m")
        command = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            "--name", os.path.splitext(os.path.basename(script_path))[0],
            script_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"\033[32m[*] Finished compiling '{os.path.basename(script_path)}'.\033[0m")

    def find_all_scripts(self):
        """Find all Python scripts in the working directory, excluding the compiler itself."""
        py_files = glob(os.path.join(self.directory, "*.py"))
        compiler_script = os.path.abspath(__file__)
        return [f for f in py_files if os.path.abspath(f) != compiler_script]

    def show_menu(self, scripts):
        """Display all detected Python scripts and prompt the user to choose one."""
        print("\n\033[36m[*] Python scripts detected in this directory:\033[0m\n")
        for idx, script in enumerate(scripts, start=1):
            print(f"  \033[36m{idx}. {os.path.basename(script)}\033[0m")
        while True:
            choice = input("\nEnter the number of the file you want to compile: ")
            if not choice.isdigit():
                print("\033[31m[!] Please enter a valid number.\033[0m")
                continue
            choice = int(choice)
            if 1 <= choice <= len(scripts):
                return scripts[choice - 1]
            else:
                print("\033[31m[!] Number out of range. Try again.\033[0m")

    def run(self):
        """Main entry point — print banner, list scripts, and compile the selected one."""
        print_gradient_banner(BANNER)
        scripts = self.find_all_scripts()
        if not scripts:
            print("\033[33m[*] No Python scripts found to compile.\033[0m")
            return
        script_to_compile = self.show_menu(scripts)
        self.compile_script(script_to_compile)


# Execute the compiler
if __name__ == "__main__":
    compiler = PythonToExeCompiler()
    compiler.run()
