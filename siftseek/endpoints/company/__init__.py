"""
The siftseek.endpoints.company __init__.py file creates the company blueprint and
imports its routes.
"""

from flask import Blueprint

company = Blueprint("company", __name__)

from siftseek.endpoints.company import company_views
