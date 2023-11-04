from datetime import datetime

from flask import request, jsonify, abort
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from . import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.post("/profile")
def post_profile():
    new_profile = seeker_schema.load(request.get_json())
    db.session.add(new_profile)
    db.session.commit()
    return seeker_schema.dump(new_profile), 201


@seeker.get("/profile/<int:id>")
def get_profile(id):
    seeker_profile = Seeker.query.get_or_404(id)
    return seeker_schema.jsonify(seeker_profile), 200
