from flask import jsonify

from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.get("/profile/<int:id>")
def get_profile(id):
    seeker_profile = Seeker.query.get_or_404(id)
    return seeker_schema.jsonify(seeker_profile), 200
