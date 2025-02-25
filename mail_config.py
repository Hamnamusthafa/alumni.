from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def init_mail(app):
    """Initialize Flask-Mail with the given app."""
    mail.init_app(app)

def send_otp_email(email, otp):
    """Send OTP email using Flask-Mail."""
    with current_app.app_context():
        msg = Message(
            subject='Your OTP Code',
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = f'Your OTP code for verification is: {otp}'
        
        try:
            print(f"📧 Attempting to send email to {email}...")
            mail.send(msg)
            print(f"✅ Email successfully sent to {email}")
        except Exception as e:
            print(f"❌ Email sending failed: {str(e)}")  # Debugging log
