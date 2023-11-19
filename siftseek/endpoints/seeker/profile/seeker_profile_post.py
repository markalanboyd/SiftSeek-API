from flask import Response, request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.post("/profile")
def post_profile() -> tuple[Response, int]:
    """
    Posts a new seeker profile.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): The seeker's new profile.
            - (int): HTTP status code. 201 if successfully posted, 400 if any
                marshmallow schema validation errors.

    Raises:
        ValidationError: If `updated_profile` fails to validate with the marshmallow schema.
        SQLAlchemyError: If there is an error during the database operation.
    """
    try:
        new_profile = seeker_schema.load(request.get_json())
        db.session.add(new_profile)
        db.session.commit()
        return seeker_schema.dump(new_profile), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
