"""
The siftseek.models db.py file initializes the SQLAlchemy database.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
