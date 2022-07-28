import functools
import os

from flask import Flask, render_template, redirect, session, flash, url_for, request, g
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db
    db.init_app(app)
    migrate = Migrate(app,db)

    @app.errorhandler(404)
    def page_not_found(e):
        return "page not found", 404

    return app

