from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.application_schema import application_schema


@seeker.post("/apply/<int:seeker_id>")
def apply_for_job(seeker_id):
    try:
        application_data = request.get_json()
        application_data["seeker_id"] = seeker_id

        new_application = application_schema.load(application_data)
        db.session.add(new_application)
        db.session.commit()

        return application_schema.dump(new_application), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
