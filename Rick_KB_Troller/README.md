# 🎹 KB_Troller
*Part of the [Rick_Ware](https://github.com/sug023/Rick_Ware) toolkit*

KB_Troller is a **keyboard-triggered prank tool** intended for **educational and authorized security testing purposes only**.  
It opens a URL and optionally raises system volume when a random letter is pressed. 💻🎉  

> ⚠️ Use only on systems you own or have explicit permission to test. Unauthorized use is illegal.

---

## ⚙️ Features

✅ **Random letter trigger** — Executes actions when a specific letter is pressed.  
✅ **URL opener** — Opens a configured link in the default browser.  
✅ **Volume control** — Optionally raises system volume on Windows.  
✅ **Persistence** — Can copy itself to Windows Startup folder.  
✅ **Threaded debounce** — Prevents multiple triggers on a single key press.  
✅ **Debug mode** — Shows verbose messages for testing.  

---

## 🧩 Requirements

- 🐍 **Python 3.7+**  
- 📦 **pip**  
- 🪟 **Windows OS** (for volume control and persistence)  
- 🖱️ **pynput** (`pip install pynput`)  
- ⚙️ **Winshell** (`pip install winshell`) (optional, for startup persistence)  

---

## 📁 Installation

Clone the Rick_Ware repository and navigate to this tool's folder:  

```bash
git clone https://github.com/sug023/Rick_Ware
cd Rick_Ware/KB_Troller
```

Or download the `KB_Troller.py` file directly.

---

## 🚀 Usage

1. Open `KB_Troller.py` in Python.  
2. Configure parameters in the constructor:  
   - `url`: URL to open when the target letter is pressed.  
   - `vol`: `True` to increase volume.  
   - `persistence`: `True` to copy script to Windows Startup.  
   - `debug`: `True` to print debug messages.  
3. Run the script:

```bash
python KB_Troller.py
```

4. The script listens for the random target letter and triggers actions when pressed.

---

## 🧠 How It Works

1. **Random letter selection** — Chooses a letter from a-z for triggering actions.  
2. **Keyboard monitoring** — Listens to all key presses using `pynput`.  
3. **Debounce** — Prevents multiple triggers from a single press.  
4. **Actions** — Opens a URL and optionally raises system volume using Windows API.  
5. **Persistence** — Copies itself to Startup folder if enabled.  

---

## 💡 Tips

- Use `debug=True` during testing to see key presses and actions in the console.  
- Only run on authorized machines to stay legal.  
- Combine with other Rick_Ware tools for fun or testing purposes.  

---

## ⚠️ Legal Notice

**KB_Troller is intended for ethical hacking, penetration testing, and educational purposes only.**  
Never run this on computers without explicit permission — doing so is illegal.

---

## 🧑‍💻 Author

**Developed with by [sug023](https://github.com/sug023)**  
💬 Contributions, feedback, and feature requests are welcome.

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🌟 Support

If KB_Troller helped you learn or test ideas, give the repository a ⭐ on GitHub! 🙌
