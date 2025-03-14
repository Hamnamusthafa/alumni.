from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, User, JobPost
from werkzeug.security import check_password_hash


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# ✅ Admin Login Page
@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    print("📌 Admin login page requested!")  # Prints to terminal

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        admin = User.query.filter_by(username=username, role='admin').first()

        if admin and check_password_hash(admin.password, password):
            session['admin_id'] = admin.id
            return redirect(url_for('admin.admin_dashboard'))
        else:
            return render_template('admin_login.html', error="Invalid credentials")

    return render_template('admin_login.html')

# ✅ Admin Dashboard
@admin_bp.route('/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin.admin_login'))

    users = User.query.all()  # Fetch all users
    jobs = JobPost.query.all()  # Fetch all job posts
    return render_template('admin_dashboard.html', users=users, jobs=jobs)

# ✅ Admin Post Job
@admin_bp.route('/post-job', methods=['POST'])
def post_job():
    if 'admin_id' not in session:
        return redirect(url_for('admin.admin_login'))

    title = request.form['title']
    description = request.form['description']
    admin_id = session['admin_id']

    new_job = JobPost(title=title, description=description, posted_by=admin_id)
    db.session.add(new_job)
    db.session.commit()

    return redirect(url_for('admin.admin_dashboard'))

# ✅ Admin Logout
@admin_bp.route('/logout')
def admin_logout():
    session.pop('admin_id', None)
    return redirect(url_for('admin.admin_login'))
