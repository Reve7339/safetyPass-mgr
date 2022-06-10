from ast import Pass
from app.tables import db, User, Passwords


def get_user(username):
    user = User.query.filter_by(username=username).first()
    return user

def register_user(UserData):
    user = User(username = UserData.id,
                password = UserData.password,
                first_name = UserData.first_name,
                last_name = UserData.last_name)
    db.session.add(user)
    db.session.commit()

def register_password(username, description, password_hash, key):
    user_id = get_user(username)
    password = Passwords(
        description = description,
        password_hash = password_hash,
        user_id = user_id.id,
        fernet_key = key
    )
    db.session.add(password)
    db.session.commit()

def get_passwords(user_id):
    passwords = Passwords.query.filter_by(user_id=user_id).all()
    return passwords