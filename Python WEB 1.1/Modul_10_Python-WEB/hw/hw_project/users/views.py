# views.py
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    MONGO_URI='mongodb://localhost:27017/myDatabase',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

def get_db():
    client = MongoClient(app.config['MONGO_URI'])
    return client.myDatabase

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.users.find_one({'username': username}) is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.users.insert_one({'username': username, 'password': generate_password_hash(password)})
            return redirect(url_for('login'))

        flash(error)

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.users.find_one({'username': username})

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = str(user['_id'])
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()