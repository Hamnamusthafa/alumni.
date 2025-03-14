from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from mail_config import init_mail, send_otp_email
<<<<<<< HEAD
from models import db, User, JobPost  # ✅ Import JobPost

import random
from werkzeug.security import check_password_hash, generate_password_hash

from admin_routes import admin_bp  


=======
from models import db, User
import random
from werkzeug.security import check_password_hash
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
init_mail(app)  # ✅ Initialize Flask-Mail here
<<<<<<< HEAD
app.register_blueprint(admin_bp)

# ✅ Home Page
@app.route('/')
def home():
    if 'admin_id' in session:  # ✅ If Admin is logged in, go to Admin Dashboard
        return redirect(url_for('admin.admin_dashboard'))  # Updated URL for admin dashboard


    logged_in = 'user_id' in session  # Check if user is logged in
    jobs = JobPost.query.order_by(JobPost.post_date.desc()).all()
    return render_template('home.html', logged_in=logged_in, jobs=jobs)
=======

# ✅ Home Page
@app.route('/')
def index():
    return render_template('index.html')
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15

@app.route('/profile')
def profile():


    if 'user_id' not in session:
        return redirect(url_for('login'))
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
<<<<<<< HEAD
=======
        

>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15

        password = request.form['password']
        print(f"🔍 Login attempt for: {username}")
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            print("✅ Login successful!")
<<<<<<< HEAD
            return redirect(url_for('home'))
=======
            return redirect(url_for('index'))
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15
        else:
            print("❌ Invalid username or password")
            return render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

# ✅ Signup Route (Handles   POST)

@app.route('/signup')
<<<<<<< HEAD
def signup_page():
=======
def sign_up():
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15
    return render_template('signup.html')



@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
<<<<<<< HEAD
    role = request.form.get('role')  # Get role from signup form

    print(f"📩 Received signup request for email: {email}, role: {role}")

    user = User.query.filter_by(email=email, role=role).first()  # Check both email and role


    if not user:
        return jsonify({"error": "Email and role combination not found. Contact admin to register."}), 400

=======

    print(f"📩 Received signup request for email: {email}")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Email not found. Contact admin to register."}), 400
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15

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

<<<<<<< HEAD


=======
>>>>>>> 973bbe277ebe69e4a919c6a5741100f195a2ee15
# ✅ Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True )