import os
import secrets

mysqldb = os.environ.get("MYSQSL_URL")

if mysqldb is None:
    mysqldb = '127.0.0.1:33060'
    database = 'python-flask'
else:
    database = 'sys'

print(mysqldb, database)

secretkey = secrets.token_hex(16)

class Config:
    SECRET_KEY = secretkey
    SERVER_NAME = '127.0.0.1:8080'
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:secret@{mysqldb}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False