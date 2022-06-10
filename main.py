from flask import request, make_response, redirect, render_template, session
import unittest
from app import create_app
from app.tables import db, User
from flask_login import login_required, current_user

app = create_app()
app.app_context().push()

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a productor']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    }

    return render_template('hello.html', **context)

if __name__ == '__main__':
    #(username, password, first_name, last_name)
    # db.drop_all()
    # db.create_all()
    # user1 = User(username='admin', password='1234', first_name='yerry', last_name='hinojosa')
    # user2 = User(username='reve', password='5678', first_name='ivan', last_name='zegarra')
    # user3 = User(username='root', password='qwerty', first_name='arch', last_name='rearch')
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(user3)
    # db.session.commit()
    app.run()