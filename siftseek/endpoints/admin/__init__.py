"""
The siftseek.endpoints.admin __init__.py file creates the admin blueprint and
imports its routes.
"""

from flask import Blueprint

admin = Blueprint("admin", __name__)

from siftseek.endpoints.admin import admin_endpoints
