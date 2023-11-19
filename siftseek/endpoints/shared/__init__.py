"""
The siftseek.endpoints.shared __init__.py file creates the shared blueprint and
imports its routes.
"""

from flask import Blueprint

shared = Blueprint("shared", __name__)

from siftseek.endpoints.shared import shared_endpoints
