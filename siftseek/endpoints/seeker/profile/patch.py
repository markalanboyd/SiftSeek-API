from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_or_abort
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.patch("/profile/<int:id>")
def patch_profile(id):
    existing_profile = get_or_abort(Seeker, id)
    try:
        updated_profile = seeker_schema.load(
            request.get_json(), instance=existing_profile, partial=True
        )
        db.session.commit()
        return seeker_schema.dump(updated_profile), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
