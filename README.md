# Rick_Ware 🚀

**A compact toolkit of small, educational security & automation utilities.** These are simple, self-contained Python scripts meant for learning, demos and authorized security testing — **not** for malicious use. ⚠️

> **Warning:** Use these tools only on systems you own or have explicit written permission to test. Unauthorized use is illegal and could cause harm. The author is not responsible for misuse. 🙏

---

## 📚 Quick overview

Rick_Ware collects tiny Python tools that demonstrate concepts like:

- sending email programmatically (SMTP),
    
- listening to keyboard events,
    
- creating a simple persistence helper on Windows,
    
- packaging Python scripts into single-file executables.
    

Each tool lives in its own folder and includes an internal README with specific instructions. The repo is aimed at people who want to experiment safely in controlled labs (VMs, isolated networks, CTFs, etc.). 🧪🖥️

---

## 🔧 Included tools

1. **EmailBomber** — Email stress/testing tool (multi-account).  
    _Folder:_ `EmailBomber/`  
    _Use:_ Controlled testing of mailbox behavior (rate limits, filtering). ✉️
    
2. **KB_Troller** — Keyboard-triggered demo/prank.  
    _Folder:_ `KB_Troller/`  
    _Use:_ Listens for a random letter and opens a URL / optionally raises volume. For local demos only. 🎹📣
    
3. **KeyLogger** (PersistentKeyLogger + KeyLogger) — Keystroke capture for testing.  
    _Folder/file:_ `KeyLogger/`  
    _Use:_ Demonstrates keyboard monitoring and optional posting to a test webhook. Only for lab use. 🔒📝
    
4. **PythonToExeCompiler** — Helper to compile scripts into executables (PyInstaller).  
    _Folder:_ `Tools/`  
    _Use:_ Scans a folder, auto-installs missing packages, and compiles a chosen script. 🛠️📦
    

---

## ✨ Highlights (per tool)

**EmailBomber**

- Multiple-account sending (`bots.txt`)
    
- Customizable messages (`content.json`)
    
- Retry logic + configurable delays
    
- Input validation and friendly CLI banner
    

**KB_Troller**

- Random trigger letter
    
- Opens a link in the default browser
    
- Optional Windows volume control & startup persistence
    
- Debug mode for testing
    

**KeyLogger**

- Aggregates keypresses and formats special keys
    
- Optional webhook push on Enter
    
- Simple persistence helper that copies the script to Startup on Windows
    

**PythonToExeCompiler**

- Pretty gradient banner for UX
    
- Auto-detects imports via `ast` and installs missing packages
    
- Installs PyInstaller if needed and builds `--onefile` `--noconsole` executables
    

---

## ✅ Requirements (global)

- **Python 3.7+**
    
- `pip`
    
- Many Windows-specific features assume a Windows host (volume control, Startup persistence). If you’re on Linux/macOS, those parts may be no-ops. 🪟❌
    

Common Python packages used across tools (installed per-tool when needed):

- `pynput`, `winshell`, `requests`, `colorama`, `pyinstaller`
    

> Tip: Follow each tool’s README for exact dependencies and examples. 📄

---

## ⚙️ Quick install

```bash
git clone https://github.com/sug023/Rick_Ware.git
cd Rick_Ware
```

Install some helpful utilities (optional):

```bash
pip install --upgrade pip
pip install colorama requests
```

Then go into any tool folder and follow its README to install the rest. 🧭

---

## 🚀 Quick usage (short)

**EmailBomber**

1. Fill `bots.txt` (`email/app_password`).
    
2. Create `content.json` with messages.
    
3. Run `python EmailBomber.py` and follow prompts.
    

**KB_Troller**

1. Configure `url`, `vol`, `persistence`, `debug` in `KB_Troller.py`.
    
2. Run `python KB_Troller.py` and press the random target key. 🎯
    

**KeyLogger**

1. Set `WEBHOOK_URL` and `DEBUG` in the script (use test endpoints).
    
2. Run `python keylogger_script.py` — it will send on Enter. ⚙️
    

**PythonToExeCompiler**

1. Put compiler in folder with scripts.
    
2. Run `python PythonToExeCompiler.py` and pick a script to compile.
    

---

## 🗂️ Recommended repo layout

```
Rick_Ware/
├─ EmailBomber/
│  ├─ EmailBomber.py
│  ├─ README.md
│  ├─ bots.txt.example
│  └─ content.json.example
├─ KB_Troller/
│  ├─ KB_Troller.py
│  └─ README.md
├─ KeyLogger/
│  ├─ keylogger.py
│  └─ README.md
├─ Tools/
│  └─ PythonToExeCompiler.py
├─ README.md      <-- this file
└─ LICENSE
```

---

## ⚖️ Safety, ethics & laws

These tools can be misused. Please don’t. 🙅‍♂️

- Only test in environments you control or have explicit permission to use.
    
- Keyloggers, spam tools and persistence mechanisms can be illegal.
    
- Always obtain written consent for penetration tests or user-facing demos.
    

If you’re learning: use VMs, disposable accounts, and local webhooks (or a private server) for testing. 🧰

---

## 🤝 Contributing

Contributions are welcome — especially docs, safer defaults, and examples. Please:

- Keep PRs focused and well-tested.
    
- Add examples or configs when you add features.
    
- Avoid adding stealthy or malicious features. ✋
    

Consider adding `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` if you accept outside contributions.

---

## ✍️ Author

**sug023** — [https://github.com/sug023](https://github.com/sug023)  
If this repo helped you, a ⭐ is appreciated! ⭐

---

## 📄 License

MIT License — see `LICENSE`.

---

If you want, I can also:

- add badges (build / license / python),
    
- include example `bots.txt` and `content.json` files, or
    
- generate `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` templates.
    

Tell me which and I’ll update the same `README.md` file. 😊