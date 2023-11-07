from flask import jsonify

from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_or_abort
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.get("/profile/<int:id>")
def get_profile(id):
    seeker_profile = get_or_abort(Seeker, id)
    return seeker_schema.jsonify(seeker_profile), 200
