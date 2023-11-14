"""
The siftseek.endpoints __init__.py file imports all of the endpoint blueprints
and inserts them into the register_blueprints function which is called by the
app factory at startup.
"""

from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.company import company
from siftseek.endpoints.admin import admin
from siftseek.endpoints.shared import shared


def register_blueprints(app):
    app.register_blueprint(seeker, url_prefix="/seeker")
    app.register_blueprint(company, url_prefix="/company")
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(shared, url_prefix="/shared")
