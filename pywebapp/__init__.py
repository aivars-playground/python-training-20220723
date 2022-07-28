import os

from distutils.command.config import config
from flask import Flask, render_template, redirect, session, flash, url_for, request
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default = 'dev')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db, User

    db.init_app(app)
    migrate = Migrate(app,db)
    
    @app.route('/sign_up', methods=('GET', 'POST'))
    def sign_up():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            error = None
            if not username:
                error = 'Username is required'
            elif not password:
                error = 'Password is required'
            elif User.query.filter_by(username = username).first():
                error = 'User exists'

            if error is None:
                user = User(username = username, password = generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                flash('Sucessfully signed up', 'success')
                return redirect(url_for('log_in'))
            else:
                flash(error, 'error')

        return render_template('sign_up.html')

    @app.route('/log_in', methods=('GET', 'POST'))
    def log_in():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            error = None
            if not username:
                error = 'Username is required'

            user = User.query.filter_by(username=username).first()

            if not user or not check_password_hash(user.password, password):
                error = 'Username or Password is incorrect'

            if error is None:
                session.clear()
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash(error, 'error')

        return render_template('log_in.html')

    @app.route('/log_out', methods=('GET', 'DELETE'))
    def log_out():
        session.clear()
        flash('Sucessfully logged out', 'success')
        return redirect(url_for('log_in'))


    @app.route('/')
    def index():
        return 'Index'

    return app
