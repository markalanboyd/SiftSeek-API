from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.post("/profile")
def post_profile():
    try:
        new_profile = seeker_schema.load(request.get_json())
        db.session.add(new_profile)
        db.session.commit()
        return seeker_schema.dump(new_profile), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
