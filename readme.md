# 🔐 Secure Vault System with Intruder Detection

A security-focused desktop application built using Python that protects sensitive folders and detects unauthorized access attempts by capturing images, recording videos, and sending email alerts.

---

## 🚀 Features

- 🔑 Secure password authentication using bcrypt
- 📁 Hidden folder protection (auto hide/unhide)
- 📸 Intruder image capture on failed attempts
- 🎥 Video recording after multiple failed attempts
- 📧 Email alert system with captured evidence
- 🔒 Auto-lock system after 3 incorrect attempts
- 🧾 Activity logging using SQLite database
- 🎨 Modern UI built with Tkinter

---

## 🧠 How It Works

1. User clicks **Enter Password**
2. If password is correct:
   - Secret folder is unhidden and opened
   - Folder auto-hides after a few seconds
3. If password is incorrect:
   - Failed attempts are tracked
4. After 3 failed attempts:
   - Intruder image is captured
   - Video recording starts
   - Email alert is sent with evidence
   - System locks for 30 seconds

---

## 📂 Project Structure
project/
│
├── main.py
│
├── ui/
│ └── app.py
│
├── security/
│ ├── auth.py
│ ├── file_protection.py
│ 
│
├── camera/
│ └── capture.py
│
├── database/
│ └── db.py
│
├── alerts/
│ └── email.py
│
├── data/ # Captured images/videos
└── intruder.db # Logs database


---

## 🛠️ Tech Stack

- **Python**
- **Tkinter** (GUI)
- **OpenCV** (Image & Video Capture)
- **SQLite** (Database)
- **SMTP** (Email alerts)
- **bcrypt** (Password security)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/secure-vault-system.git
cd secure-vault-system

Run the application
python main.py
