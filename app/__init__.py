from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import logging
from werkzeug.exceptions import MethodNotAllowed
from flask_jwt_extended import JWTManager
from datetime import timedelta

from .extensions import db, ma


def setup_logging():
    """
    set up logging for the project
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    log_dir = os.path.join(project_root, 'log')
    os.makedirs(log_dir, exist_ok=True)

    cur_f_name = os.path.splitext(os.path.basename(__file__))[0]
    log_path = os.path.join(log_dir, f'{cur_f_name}.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s -> %(funcName)s | %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path)
        ]
    )

    logging.info('Logging setup complete')


def init_app():
    load_dotenv()

    app = Flask(__name__)

    app.secret_key = os.environ.get('APP_SECRET_KEY')
    access_token_expiry_in_min = int(os.environ.get('ACCESS_TOKEN_EXPIRY_IN_MIN'))
    refresh_token_expiry_in_min = int(os.environ.get('REFRESH_TOKEN_EXPIRY_IN_MIN'))

    app.config['JWT_SECRET_KEY'] = app.secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=access_token_expiry_in_min)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(minutes=refresh_token_expiry_in_min)

    JWTManager(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from app.model import User, Post

    @app.errorhandler(405)
    def handle_method_not_allowed(e: MethodNotAllowed):
        allowed = e.valid_methods if hasattr(e, 'valid_methods') else None
        return jsonify({
            'error': f'Method {request.method} not allowed on this endpoint.',
            'allowed': allowed
        })

    from .blogapp_routes import main
    from .userapp_routes import userapp

    app.register_blueprint(main)
    app.register_blueprint(userapp)

    return app