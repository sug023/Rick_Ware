# 📧 EmailBomber

*Part of the [Rick_Ware](https://github.com/sug023/Rick_Ware) toolkit*

EmailBomber is a **script for sending a barrage of emails** intended for **educational and authorized security testing purposes only**.  
It utilizes multiple email accounts to flood a target email with messages. 📧🔥

> ⚠️ Use only on systems you own or have explicit permission to test. Unauthorized use is illegal.

---

## ⚙️ Features

✅ **Multiple account support** — Uses multiple email accounts for sending emails.  
✅ **Custom content** — Allows for customizable email subjects and messages.  
✅ **Retry mechanism** — Handles temporary SMTP errors with retry logic.  
✅ **Delay between emails** — Configurable delay to avoid detection.  
✅ **Gradient banner** — Adds a visually appealing gradient banner.  
✅ **File validation** — Ensures that credentials and content files are valid and exist.  

---

## 🧩 Requirements

- 🐍 **Python 3.7+**  
- 📦 **pip**  
- 📧 **smtplib**  
- 📄 **email.mime.text**  
- 📄 **email.mime.multipart**  
- 🪟 **Windows OS** (optional, for better user experience)  
- 📚 **json**  
- 📚 **os**  
- 📚 **re**  
- 📚 **pathlib**  
- 📚 **sys**  
- 📚 **time**  

---

## 📁 Installation

Clone the Rick_Ware repository and navigate to this tool's folder:  

```bash
git clone https://github.com/sug023/Rick_Ware
cd Rick_Ware/EmailBomber
```


---

## 🚀 Usage

1. Prepare the `bots.txt` file with email credentials in the format `email/app_password`.
2. Prepare the `content.json` file with email content in JSON format.
3. Run the script:

```bash
python EmailBomber.py
```

1. Follow the prompts to enter the target email, file paths, and delay settings.
2. The script will start sending emails according to the specified configuration.

---

## 🧠 How It Works

1. **Read credentials** — Loads email credentials from `bots.txt`.
2. **Read content** — Loads email content from `content.json`.
3. **SMTP connection** — Connects to the SMTP server (e.g., Gmail).
4. **Email sending** — Sends emails using the provided credentials and content.
5. **Error handling** — Manages authentication and SMTP errors with retries.

---

## 💡 Tips

- Ensure that the email accounts used have app passwords enabled for better security.
- Customize the delay between emails to avoid detection by spam filters.
- Use the gradient banner for a more engaging user experience.

---

## ⚠️ Legal Notice

**EmailBomber is intended for ethical hacking, penetration testing, and educational purposes only.**  
Never run this on computers without explicit permission — doing so is illegal.

---

## 🧑‍💻 Author

**Developed with by sug023**  
💬 Contributions, feedback, and feature requests are welcome.

---

## 📜 License

Licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🌟 Support

If EmailBomber helped you learn or test ideas, give the repository a ⭐ on GitHub! 🙌