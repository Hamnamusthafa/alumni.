from mail_config import send_otp_email
from app import app  # ✅ Import Flask app

# ✅ Set up an application context
with app.app_context():
    send_otp_email('hamnat211@gmail.com', '123456')  # Replace with your email
