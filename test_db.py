from models import db
from app import app
from sqlalchemy.sql import text  # ✅ Import text to execute raw SQL

with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))  # ✅ Wrap query in text()
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")  # ✅ Print actual error
