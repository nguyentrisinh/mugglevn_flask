import os
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
admin = Admin()

import app.routes
from .api import *
from admin import *



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config.APP_SETTINGS)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Config.init_app(app)

    db.init_app(app)

    admin.init_app(app)

    # Create app blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create Api Resource
    from .api import api_bp as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


