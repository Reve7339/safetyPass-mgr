import secrets

secretkey = secrets.token_hex(16)

class Config:
    SECRET_KEY = secretkey
    SERVER_NAME = '127.0.0.1:8080'
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secret@127.0.0.1:33060/python-flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False