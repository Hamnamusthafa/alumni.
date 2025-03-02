from mail_config import send_otp_email
from app import app, db
from models import User

# ✅ Set up an application context
with app.app_context():
    test_email = 'ha@gmail.com'  # Replace with the email you want to test

    # ✅ Check if the email exists in the database
    user = User.query.filter_by(email=test_email).first()

    if user:
        otp = '123456'  # You can replace this with a randomly generated OTP
        print(f"✅ Email {test_email} exists in database. Sending OTP...")
        send_otp_email(test_email, otp)
        print("✅ OTP email sent successfully!")
    else:
        print(f"❌ Email {test_email} does not exist in the database. No email sent.")
