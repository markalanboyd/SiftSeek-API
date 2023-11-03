from flask import Blueprint

shared = Blueprint("shared", __name__)

from . import shared_views
