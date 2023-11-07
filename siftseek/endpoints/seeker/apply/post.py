from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.application_schema import application_schema


@seeker.post("/apply")
def apply_for_job():
    try:
        new_application = application_schema.load(request.get_json())
        db.session.add(new_application)
        db.session.commit()
        return application_schema.dump(new_application), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
