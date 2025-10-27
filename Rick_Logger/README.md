# 📝 Rick_Logger 🔑
*Part of the [Rick_Ware](https://github.com/sug023/Rick_Ware) toolkit*

Rick_Logger is a **persistent keylogging and monitoring tool** intended for **educational and authorized security testing purposes only**.  
It captures keystrokes and can send them to a webhook endpoint, helping developers and security professionals analyze input patterns during authorized testing. 💻🔒  

> ⚠️ Use only on systems you own or have explicit permission to test. Unauthorized use is illegal.

---

## ⚙️ Features

✅ **Persistent execution** — Automatically adds itself to Windows startup.  
✅ **Keystroke monitoring** — Records all key presses in real-time.  
✅ **Webhook integration** — Sends captured keystrokes to a specified endpoint.  
✅ **Modifier key detection** — Detects Ctrl, Alt, and Shift combinations.  
✅ **Threaded architecture** — Runs key listening in a background thread.  
✅ **Debug mode** — Verbose output for testing and monitoring.  

---

## 🧩 Requirements

- 🐍 **Python 3.7+**  
- 📦 **pip**  
- 🪟 **Windows OS**  
- 🖱️ **Keyboard library** (`pip install keyboard`)  
- 📡 **Requests library** (`pip install requests`)  
- ⚙️ **Winshell** (`pip install winshell`)  

> The script will also automatically handle debug messages when enabled.

---

## 📁 Installation

Clone the main Rick_Ware repository and navigate to this tool’s directory:  

```bash
git clone https://github.com/sug023/Rick_Ware
cd Rick_Ware/Rick_Logger
```

Or download the `Rick_Logger.py` file directly.

---

## 🚀 Usage

1. Open `Rick_Logger.py` in Python.  
2. Set your **webhook URL** in the `WEBHOOK_URL` variable.  
3. Enable `DEBUG = True` if you want verbose logs.  
4. Run the script:

```bash
python Rick_Logger.py
```

5. The script will start listening for key input in the background and send formatted keystrokes to the webhook endpoint.  

> The keylogger will also try to persist by copying itself to the Windows startup folder.

---

## 🧠 How It Works

1. **Persistence**: Copies the script or executable to the Windows startup directory.  
2. **Key monitoring**: Listens to all key events using the `keyboard` library.  
3. **Data formatting**: Converts keys and modifiers into readable strings (e.g., `[CTRL + A]`, `[ENTER]`).  
4. **Webhook delivery**: Sends formatted keystrokes to the configured webhook.  
5. **Threading**: Runs the key listening loop in a daemon thread, so the main program remains responsive.  

---

## 🧰 Example Output

```text
[ LISTENING FOR KEY INPUTS ]
[DEBUG] Key pressed: a
[DEBUG] Key pressed: enter
[+] Data sent successfully (HTTP 204) [+]
```

---

## 💡 Tips

- Use `DEBUG = True` during testing to see key presses and webhook delivery.  
- Only run on authorized machines to stay compliant with the law.  
- For advanced monitoring, you can combine this with other Rick_Ware tools.  

---

## ⚠️ Legal Notice

**Rick_Logger is intended for ethical hacking, penetration testing, and educational purposes only.**  
Never run this on computers without explicit permission — doing so is illegal and punishable by law.

---

## 🧑‍💻 Author

**Developed with by [sug023](https://github.com/sug023)**  
💬 Contributions, feedback, and feature requests are welcome.

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🌟 Support the Project

If Rick_Logger helped you learn or streamline testing, give the repository a ⭐ on GitHub! 🙌  
Your support helps grow the **Rick_Ware toolkit**.