from flask import Flask
from models.db import db
from models import Seeker


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///siftseek.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app