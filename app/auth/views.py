from flask import render_template, flash, url_for, redirect
from flask_login import login_required, login_user, logout_user
from . import auth
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, SignUpForm
from app.mysql_service import get_user, register_user
from app.user_model import UserData, UserModel

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = get_user(username)

        if user is not None:
            user_password = user.password
            if check_password_hash(user_password, password):
                user_data = UserData(
                    user.username,
                    user.password,
                    user.first_name,
                    user.last_name
                )
                user_model = UserModel(user_data)
                login_user(user_model)
                flash('Welcome', 'message')
                return redirect(url_for('hello'))
            else:
                flash('La contraseña es incorrecta', 'error')
        else:
            flash('El usuario no existe', 'error')

    return render_template('login.html', **context)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        user = get_user(username)
        if user is None:
            first_name = signup_form.first_name.data
            last_name = signup_form.last_name.data
            password_hash = generate_password_hash(password)
            user_data = UserData(
                username,
                password_hash,
                first_name,
                last_name
            )
            register_user(user_data)
            user_model = UserModel(user_data)
            login_user(user_model)
            flash('Welcome', 'message')
            return redirect(url_for('hello'))
        else:
            flash('The user already exists', 'message')


    return render_template('signup.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto', 'message')
    return redirect(url_for('auth.login'))