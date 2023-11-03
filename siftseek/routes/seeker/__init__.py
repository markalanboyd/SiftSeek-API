from flask import Blueprint

seeker = Blueprint("seeker", __name__)

from . import seeker_views
