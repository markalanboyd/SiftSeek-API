from .seeker import seeker
from .company import company
from .admin import admin
from .shared import shared


def register_blueprints(app):
    app.register_blueprint(seeker, url_prefix="/seeker")
    app.register_blueprint(company, url_prefix="/company")
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(shared, url_prefix="/shared")
