import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import os
import time

from security.auth import check_password
from camera.capture import capture_image, record_video
from database.db import insert_log, init_db
from alerts.email import send_email
from security.file_protection import hide_file, unhide_file, open_file

STORE_DIR = "data"
HASHED_PASSWORD = b'$2b$12$8otTnY1Mz49bM0ZnBkgLEe6Bx54s/8HOVMOyavaUmBh.KBpX0jOCK'

SECRET_PATH = r"C:\Users\Pooja Abhonkar\Desktop\SecretFolder"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Vault System")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2f")  # dark theme

        os.makedirs(STORE_DIR, exist_ok=True)

        # 🔒 Hide folder at start
        if os.path.exists(SECRET_PATH):
            hide_file(SECRET_PATH)

        init_db()

        self.failed_attempts = 0
        self.locked = False

        # 🛡️ ICON
        self.logo = tk.Label(
            root,
            text="🛡️",
            font=("Arial", 40),
            bg="#1e1e2f"
        )
        self.logo.pack(pady=10)

        # 🔐 TITLE
        self.title_label = tk.Label(
            root,
            text="Secure Vault System",
            font=("Segoe UI", 20, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.title_label.pack(pady=5)

        # 📦 CARD FRAME
        self.card = tk.Frame(
            root,
            bg="#2c2c3e",
            bd=0
        )
        self.card.pack(pady=30, ipadx=30, ipady=30)

        # ℹ️ INFO TEXT
        self.info = tk.Label(
            self.card,
            text="Enter password to access secure folder",
            font=("Segoe UI", 11),
            bg="#2c2c3e",
            fg="#cccccc"
        )
        self.info.pack(pady=10)

        # 🔘 BUTTON
        self.btn = tk.Button(
            self.card,
            text="🔓 Enter Password",
            command=self.access_secret,
            font=("Segoe UI", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            padx=20,
            pady=8,
            bd=0,
            cursor="hand2"
        )
        self.btn.pack(pady=20)

        # 🎯 HOVER EFFECT
        self.btn.bind("<Enter>", lambda e: self.btn.config(bg="#45a049"))
        self.btn.bind("<Leave>", lambda e: self.btn.config(bg="#4CAF50"))

        # 🧾 FOOTER
        self.footer = tk.Label(
            root,
            text="Intruder Detection Enabled",
            font=("Segoe UI", 9),
            bg="#1e1e2f",
            fg="#888"
        )
        self.footer.pack(side="bottom", pady=10)

    # 🔐 MAIN FUNCTION
    def access_secret(self):
        if self.locked:
            messagebox.showwarning("Locked", "System locked!")
            return

        pwd = simpledialog.askstring("Access Vault", "Enter Password:")

        if pwd is None:
            return

        try:
            if check_password(pwd, HASHED_PASSWORD):
                print("✅ Correct password")

                if os.path.exists(SECRET_PATH):
                    unhide_file(SECRET_PATH)
                    open_file(SECRET_PATH)

                    threading.Thread(target=self.auto_hide_secret).start()

                insert_log("SUCCESS", "Folder opened")

                messagebox.showinfo("Access", "Access Granted")
                self.failed_attempts = 0

            else:
                print("❌ Wrong password")

                self.failed_attempts += 1
                insert_log("FAILED", None)

                # 🚨 ONLY ON 3rd ATTEMPT
                if self.failed_attempts >= 3:
                    self.handle_intruder()
                else:
                    messagebox.showerror(
                        "Error",
                        f"Wrong Password! Attempt {self.failed_attempts}/3"
                    )

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", str(e))

    # 🚨 Intruder action (3rd attempt)
    def handle_intruder(self):
        messagebox.showwarning("Alert", "Intruder detected! Capturing evidence...")

        # 📸 Capture image
        img_path = capture_image(STORE_DIR)

        # 📧 Send image immediately
        if img_path:
            send_email(img_path)

        # 🎥 Record video in background
        threading.Thread(target=self.record_intruder).start()

        # 🔒 Lock system
        self.lock_system()

    # 🎥 Record video + email
    def record_intruder(self):
        video_path = record_video(STORE_DIR, 15)

        if video_path:
            send_email(video_path)

    # 🔒 Auto hide folder
    def auto_hide_secret(self):
        time.sleep(10)
        if os.path.exists(SECRET_PATH):
            hide_file(SECRET_PATH)
            print("Secret folder hidden again")

    # 🔒 Lock system
    def lock_system(self):
        self.locked = True
        messagebox.showwarning("Locked", "System locked for 30 seconds!")

        self.root.after(30000, self.unlock)

    # 🔓 Unlock
    def unlock(self):
        self.locked = False
        self.failed_attempts = 0
        messagebox.showinfo("Unlocked", "Try again")