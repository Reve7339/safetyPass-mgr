from flask import render_template, request, redirect, url_for
from app import create_app
from app.tables import db
from flask_login import login_required, current_user
from app.mysql_service import  get_user, register_password, get_passwords
from cryptography.fernet import  Fernet
import string
import random

app = create_app()
app.app_context().push()

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    username = current_user.id
    if request.method == 'POST':
        data = request.form
        description = data.get('description')
        length_pass = data.get('length_pass')
        length_pass = int(length_pass)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length_pass))
        key = Fernet.generate_key()
        fernet = Fernet(key)
        password_hash = fernet.encrypt(password.encode())
        register_password(username, description, password_hash, key)
        return redirect(url_for('index'))
    user_id = get_user(username)
    user_id = user_id.id
    passwords_data = get_passwords(user_id)
    passwords_decripted = list()
    for item in passwords_data:
        fernet = Fernet(item.fernet_key)
        passwords_decripted.append(fernet.decrypt(item.password_hash.encode()).decode())
    context = {
        'username': username,
        'passwords_data': passwords_data,
        'passwords_decripted': passwords_decripted
    }
    return render_template("index.html", **context)

if __name__ == '__main__':
    db.create_all()
    db.session.close()
    app.run()