from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Create a base class using declarative_base
Base = declarative_base()

# Initialize SQLAlchemy with the custom base class
db = SQLAlchemy(model_class=Base)
