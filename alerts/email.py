import smtplib
from email.message import EmailMessage
import os

def send_email(file_path):
    try:
        EMAIL = "abhishekkasnale6@gmail.com"
        PASSWORD = "eivcuntjupdlkvdi"

        msg = EmailMessage()
        msg["Subject"] = "⚠️ Intruder Alert!"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        msg.set_content("Intruder detected! Check attachment.")

        # ✅ Detect file type automatically
        filename = os.path.basename(file_path)

        if file_path.endswith(".jpg"):
            maintype, subtype = "image", "jpeg"
        elif file_path.endswith(".mp4"):
            maintype, subtype = "video", "mp4"
        else:
            maintype, subtype = "application", "octet-stream"

        with open(file_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=maintype,
                subtype=subtype,
                filename=filename
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email error:", e)