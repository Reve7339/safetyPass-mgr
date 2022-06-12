import os
import secrets

mysqldb = os.environ.get("MYSQL_URL")

if mysqldb is None:
    mysqldb = '127.0.0.1:33060'

secretkey = secrets.token_hex(16)

class Config:
    SECRET_KEY = secretkey
    SERVER_NAME = '127.0.0.1:8080'
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secret@{mysqldb}/python-flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False