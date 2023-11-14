from flask import Flask
from flask_marshmallow import Marshmallow

from siftseek.logging_config import configure_logging
from siftseek.models.db import db
from siftseek.endpoints import register_blueprints
from siftseek.config import DevelopmentConfig, TestingConfig, ProductionConfig


def create_app(config_name: str) -> Flask:
    """
    Creates and configures an instance of the Flask application.

    Based on the provided configuration name, the application is set up with
    specific configurations suitable for development, testing, or production
    environments. It initializes the database and configures logging,
    marshmallow, and registers all necessary blueprints for the application's
    endpoints.

    The function also sets up the application context and creates all database
    tables necessary for the application. This setup ensures that the
    application is ready to handle requests with all its components properly
    initialized.

    Args:
        config_name (str): A string indicating the configuration to use.
            Accepts "dev", "test", or "prod" corresponding to DevelopmentConfig,
            TestingConfig, and ProductionConfig, respectively.

    Returns:
        Flask: An instance of the Flask application configured as per the
            specified environment.
    """
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
