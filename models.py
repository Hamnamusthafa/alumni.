from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)  # ✅ Changed 'name' to 'username'
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # ✅ Password stored only after OTP verification
    role = db.Column(db.String(10), nullable=False)
    academic_year = db.Column(db.String(10), nullable=False)
    otp = db.Column(db.String(6), nullable=True)  # OTP is temporary
