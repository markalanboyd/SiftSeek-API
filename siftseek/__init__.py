from flask import Flask
from flask_marshmallow import Marshmallow

from siftseek.logging_config import configure_logging
from siftseek.models.db import db
from siftseek.endpoints import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    configure_logging()

    db.init_app(app)
    ma = Marshmallow(app)

    with app.app_context():
        from siftseek.models.seeker import Seeker
        from siftseek.models.application import Application

        db.create_all()
        register_blueprints(app)

    return app
