from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from mail_config import init_mail,send_otp_email
from models import db, User
import random
from werkzeug.security import check_password_hash  # Ensure secure password checking

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
init_mail(app)  # ✅ Initialize Flask-Mail here
# ✅ Correct home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('pro.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/about')
def about():
    return render_template('about.html')

# ✅ Fixed Login Route (Handles both GET & POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):  # Check password securely
            session['user_id'] = user.id  # Store user session
            return redirect(url_for('home'))  # Redirect to home after login
        else:
            return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')  # Render login page for GET requests
@app.route('/signup')
def signin_page():
    return render_template('signup.html')
# ✅ Signup Page Route
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']

    # Check if email exists in the database
    existing_user = User.query.filter_by(email=email).first()

    if not existing_user:
        print("❌ Email not found in database.")  # Debugging log
        return jsonify({"error": "Email not found. Contact admin to register."}), 400

    # Generate OTP
    otp = str(random.randint(100000, 999999))
    print(f"🔢 Generated OTP: {otp} for {email}")  # Debugging log

    # Store OTP in the database
    existing_user.otp = otp
    db.session.commit()

    # Send OTP
    try:
        print(f"📧 Attempting to send OTP email to {email}...")  # Debugging log
        send_otp_email(email, otp)
        return jsonify({"message": "OTP sent successfully!"})
    except Exception as e:
        print(f"❌ Email sending failed: {str(e)}")  # Debugging log
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500


# ✅ Verify OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    entered_otp = request.form['otp']

    user = User.query.filter_by(email=email).first()
    if user and user.otp == entered_otp:
        return jsonify({"message": "OTP verified. Redirecting to home page!"})
    else:
        return jsonify({"error": "Invalid OTP"}), 400

# ✅ Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# ✅ `if __name__ == '__main__'` should always be at the bottom
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
