# 🐍 Python to EXE Compiler

A **fully automated Python script compiler** that converts `.py` files into standalone `.exe` executables. The script detects Python files in its directory, handles missing dependencies automatically, and compiles the selected file silently using **PyInstaller**.

---

## ✨ Features

- 🔍 **Automatic Detection:** Finds all `.py` scripts in the directory.
    
- 📝 **Interactive Menu:** Choose which file to compile via a numbered menu.
    
- 📦 **Dependency Management:** Automatically installs missing Python packages required by the target script.
    
- ⚡ **Onefile Executable:** Compiles into a single `.exe` file using `--onefile`.
    
- 🚫 **Silent Compilation:** PyInstaller output is hidden, only clean status messages are shown.
    
- ✅ **Clear Feedback:** Displays only relevant messages:
    
    - Files detected for compilation
        
    - Compiling {filename}…
        
    - Finished compiling {filename}

---

## 🛠 Requirements

- Python 3.6+
    
- `pip` installed
    

> The script will automatically install **PyInstaller** and any required packages for the target script.

---
## 📂 Directory Setup

Place the `compile_to_exe.py` script in the **same folder** as the Python scripts you want to compile:
```kotlin
/my_project
│
├─ compile_to_exe.py
├─ script1.py
├─ script2.py
└─ script3.py

```

---

## 🚀 Usage

1. Run the script:
```kotlin
python compile_to_exe.py
```

2. A menu will appear listing all Python scripts detected:
```kotlin
[*] Python scripts detected in this directory:
  1. script1.py
  2. script2.py
Enter the number of the file you want to compile:
```

3.  Enter the **number** corresponding to the file you want to compile.

4.  Compilation will begin:
```kotlin
[*] Compiling 'script1.py'...
[*] Finished compiling 'script1.py'.
```

5. The compiled `.exe` file will be located in:
```kotlin
./dist/script1.exe
```

---

## 🎨 Example Workflow

```kotlin
$ python compile_to_exe.py
[*] Python scripts detected in this directory:
  1. my_app.py
  2. utilities.py
Enter the number of the file you want to compile: 1
[*] Compiling 'my_app.py'...
[*] Finished compiling 'my_app.py'.
```

---

## 💡 Notes

- The compiler script itself (`compile_to_exe.py`) will **not** be compiled.
    
- Any external dependencies (like `requests`, `keyboard`, etc.) are automatically installed.
    
- Compilation is silent to keep the console clean.
    
- Works on Windows (PyInstaller generates `.exe` files).

---

## ⚙️ Optional Improvements

- Clean up temporary files (`build/` and `.spec`) automatically after compilation.
    
- Add support for compiling **multiple files at once**.
    
- Optional `--console` mode for debugging console-based applications.
    
- Recursive scanning of subdirectories to detect Python files.

---

## 📦 Folder Structure After Compilation

```kotlin
/my_project
│
├─ compile_to_exe.py
├─ script1.py
├─ dist/
│   └─ script1.exe
├─ build/        (PyInstaller temporary files)
└─ script1.spec  (PyInstaller spec file)
```

