import os

class Config:
    SECRET_KEY = '30245fea5eb7270eea2d9fa6a685c057173f69b25d06da0740701efac33039bd'  # Change this
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Hamna123@localhost/alumni_portal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'alumniportal123@gmail.com'  # Replace with your email
    MAIL_PASSWORD = 'rlzh sluy emuj imqv'  # Use App Password if using Gmail
