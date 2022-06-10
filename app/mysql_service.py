from app.tables import db, User


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

def get_passwords():
    pass