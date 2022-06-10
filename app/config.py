class Config:
    SECRET_KEY = 'SUPER SECRETO'
    SERVER_NAME = '127.0.0.1:8080'
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secret@127.0.0.1:33060/python-flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False