# 🐍 Python ➜ EXE Compiler 🚀  
*Part of the [Rick_Ware](https://github.com/sug023/Rick_Ware) toolkit*

Turn any Python script into a **stand-alone Windows executable (.exe)** — automatically handling dependencies, missing packages, and PyInstaller setup.  
This tool makes it effortless to share your Python apps with others, even if they don’t have Python installed. 💻✨  

---

## ⚙️ Features

✅ **Automatic dependency detection** — Scans your script for all imported modules.  
✅ **Auto-install missing packages** — Uses `pip` to install anything not already available.  
✅ **PyInstaller integration** — Compiles scripts into `.exe` files seamlessly.  
✅ **Gradient banner** — Eye-catching startup banner with RGB color fade.  
✅ **Interactive script selection menu** — Choose which `.py` file to compile from your folder.  
✅ **Error handling and clean output** — Professional and minimal console logs.  

---

## 🧩 Requirements

- 🐍 **Python 3.7+**  
- 📦 **pip** (Python package manager)  
- 🪟 **Windows OS** (for generating `.exe` executables)  

> The script will automatically install `colorama` and `pyinstaller` if they are missing.  

---

## 📁 Installation

Clone the main Rick_Ware repository and navigate to this tool’s directory:  

```bash
git clone https://github.com/sug023/Rick_Ware
cd Rick_Ware/Python_To_Exe
```

Or simply download the `.py` file directly if you only need this component.  

---

## 🚀 Usage

1. Place your **Python scripts** (`.py` files) in the **same folder** as the compiler script.  
2. Run the compiler:

```bash
python compiler.py
```

3. You’ll see a colorful gradient banner 🌈 and a list of detected Python scripts:

```
[*] Python scripts detected in this directory:

  1. app.py
  2. gui_tool.py
  3. my_project.py
```

4. Enter the number of the script you want to compile (for example: `1`).  
5. Wait a few seconds — your `.exe` will be created in the `/dist` folder 🎉  

---

## 🧠 How It Works

🔍 **1. Module scanning**  
Uses Python’s `ast` module to parse your source code and detect all imported packages.  

📦 **2. Dependency management**  
Automatically installs any missing packages using `pip`.  

⚙️ **3. Compilation**  
Invokes `PyInstaller` with `--onefile` and `--noconsole` options to build a clean standalone `.exe`.  

📁 **4. Output**  
The generated executable will appear in the `/dist` folder next to your script.  

---

## 🧰 Example Output

```bash
[*] Compiling 'my_script.py'...
[*] Finished compiling 'my_script.py'.
```

➡️ Result: `dist/my_script.exe`

---

## 🪄 Customization

You can easily adjust build parameters in the source code:  

| Option        | Description                        | Default             |
| -------------- | ---------------------------------- | ------------------- |
| `--onefile`    | Package everything into one `.exe` | ✅                   |
| `--noconsole`  | Hide console window (for GUI apps) | ✅                   |
| `--name`       | Output file name                   | Same as script name |
| `directory`    | Working directory                  | Current folder      |

---

## 💡 Tips

- To **view PyInstaller logs**, remove `stdout=subprocess.DEVNULL` and `stderr=subprocess.DEVNULL` in the code.  
- For **debug builds**, comment out `--noconsole` to keep the terminal visible.  
- Works best for simple GUI or CLI scripts — for complex frameworks, you can pass extra PyInstaller flags.  

---

## ⚠️ Notes

- Generated executables are **Windows-only**.  
- Re-running the compiler will overwrite previous builds.  
- Antivirus tools may flag new `.exe` files — this is normal for unsigned executables.  

---

## 🧑‍💻 Author

**Developed with by [sug023](https://github.com/sug023)**  
💬 Contributions, issues, and feature suggestions are always welcome!  

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and distribute.  

---

## 🌟 Star This Project!

If this tool saved you time or made your workflow easier, please consider giving it a ⭐ on GitHub!  
Your support helps keep **Rick_Ware** growing! 🙌