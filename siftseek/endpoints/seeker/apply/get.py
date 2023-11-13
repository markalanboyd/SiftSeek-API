from flask import jsonify
from marshmallow import ValidationError

from siftseek.models.seeker import Seeker
from siftseek.models.application import Application
from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import (
    get_filtered_many_or_abort,
)
from siftseek.schemas.application_schema import application_schema


@seeker.get("/apply/<int:seeker_id>")
def get_all_applications(seeker_id):
    try:
        applications = get_filtered_many_or_abort(Application, {"seeker_id": seeker_id})
        application_data = application_schema.dump(applications, many=True)
        return jsonify(application_data), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
