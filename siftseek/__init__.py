from flask import Flask
from flask_marshmallow import Marshmallow

from .models.db import db
from .routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///siftseek.db"

    db.init_app(app)
    ma = Marshmallow(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()

    return app
