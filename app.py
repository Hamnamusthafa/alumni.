from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from mail_config import init_mail, send_otp_email
from models import db, User
import random
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
init_mail(app)  # ✅ Initialize Flask-Mail here

# ✅ Home Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('pro.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/about')
def about():
    return render_template('about.html')




# ✅ Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        


        password = request.form['password']
        print(f"🔍 Login attempt for: {username}")
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            print("✅ Login successful!")
            return redirect(url_for('index'))
        else:
            print("❌ Invalid username or password")
            return render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

# ✅ Signup Route (Handles   POST)

@app.route('/signup')
def sign_up():
    return render_template('signup.html')



@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"📩 Received signup request for email: {email}")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Email not found. Contact admin to register."}), 400

    otp = str(random.randint(100000, 999999))
    user.otp = otp
    db.session.commit()

    try:
        send_otp_email(email, otp)
        session['pending_signup'] = {
            "email": email,
            "username": username,
            "password": password
        }
        return jsonify({"message": "OTP sent. Please enter the OTP to verify your account."}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500




# ✅ Verify OTP Route

from werkzeug.security import generate_password_hash
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    entered_otp = request.form['otp']
    
    user = User.query.filter_by(email=email).first()

    if user and user.otp == entered_otp:
        signup_data = session.pop('pending_signup', None)
        if not signup_data:
            return jsonify({"error": "Session expired. Please sign up again."}), 400

        user.username = signup_data["username"]
        user.password = generate_password_hash(signup_data["password"])
        user.otp = None
        db.session.commit()

        return jsonify({"message": "OTP verified. Redirecting to home page!"}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 400




# ✅ Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# ✅ Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
