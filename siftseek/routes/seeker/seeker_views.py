from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.routes.seeker import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.get("/profile/<int:id>")
def get_profile(id):
    seeker_profile = Seeker.query.get_or_404(id)
    return seeker_schema.jsonify(seeker_profile), 200


@seeker.post("/profile")
def post_profile():
    try:
        new_profile = seeker_schema.load(request.get_json())
        db.session.add(new_profile)
        db.session.commit()
        return seeker_schema.dump(new_profile), 201
    except ValidationError as e:
        return jsonify(e.messages), 400


@seeker.put("/profile/<int:id>")
def put_profile(id):
    try:
        existing_profile = Seeker.query.get_or_404(id)
        updated_profile = seeker_schema.load(
            request.get_json(), instance=existing_profile
        )
        db.session.commit()
        return seeker_schema.dump(updated_profile), 200
    except ValidationError as e:
        return jsonify(e.messages), 400


@seeker.patch("/profile/<int:id>")
def patch_profile(id):
    try:
        existing_profile = Seeker.query.get_or_404(id)
        updated_profile = seeker_schema.load(
            request.get_json(), instance=existing_profile, partial=True
        )
        db.session.commit()
        return seeker_schema.dump(updated_profile), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
