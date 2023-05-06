import os


class Config:
    SECRET_KEY = '3ce5b77f5f7fb9f1caa5d4a3930fe763'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = " @gmail.com"
    MAIL_PASSWORD = " "
