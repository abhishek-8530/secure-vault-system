# 🔐 Secure Vault System

A Python-based intruder detection system with:
- Password protection (bcrypt)
- Secret folder hiding/unlocking
- Intruder image capture
- Video recording on failed attempts
- Email alerts

## 🚀 Features
- 3 failed attempts → capture + email alert
- Folder auto-hide after access
- SQLite logging
- Thread-based video recording

## 🛠 Tech Stack
- Python
- Tkinter
- OpenCV
- SQLite
- SMTP Email

## ▶️ Run
```bash
python main.py

📦 Build EXE
pyinstaller --onefile --noconsole main.py


