from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# db variable initialization
db = SQLAlchemy()
# login_manager = LoginManager()

# local imports
from config import app_config
# from . import models

# third-party imports
import os


# def create_app(config_name):
def create_app():
    app_dir = os.path.dirname(__file__)
    print(app_dir)
    app = Flask(__name__, instance_path = os.path.dirname(app_dir) + '/instance', instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # login_manager.init_app(app)
    # login_manager.login_message = "You must be logged in to access this page."
    # login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    Bootstrap(app)

    from app.home import home as home_blueprint
    from .api import api as api_blueprint
    from app.crud import crud as crud_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(crud_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app
