from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.patch("/profile/<int:id>")
def patch_profile(id):
    existing_profile = Seeker.query.get_or_404(id)
    try:
        updated_profile = seeker_schema.load(
            request.get_json(), instance=existing_profile, partial=True
        )
        db.session.commit()
        return seeker_schema.dump(updated_profile), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
