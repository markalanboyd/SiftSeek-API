from flask import Flask
from flask_marshmallow import Marshmallow

from siftseek.logging_config import configure_logging
from siftseek.models.db import db
from siftseek.endpoints import register_blueprints
from siftseek.config import DevelopmentConfig, TestingConfig, ProductionConfig


def create_app(config_name):
    app = Flask(__name__)

    configs = {
        "dev": DevelopmentConfig,
        "test": TestingConfig,
        "prod": ProductionConfig,
    }

    app.config.from_object(configs[config_name])

    configure_logging()

    db.init_app(app)
    register_blueprints(app)
    ma = Marshmallow(app)

    with app.app_context():
        db.create_all()

    return app
