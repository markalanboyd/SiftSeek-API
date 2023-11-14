from flask import Response, request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_model_by_pk_or_abort
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.put("/profile/<int:seeker_id>")
def put_profile(seeker_id: int) -> tuple[Response, int]:
    """
    Updates an entire seeker's profile.

    Args:
        seeker_id (int): Primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): The seeker's updated profile.
            - (int): HTTP status code. 200 if successful, 404 if account has
                already been marked for deletion.

    Raises:
        HTTPException: If no instance is found, aborts the request and raises
            a 404 error.
        ValidationError: If `updated_profile` fails to validate with the marshmallow schema.
        SQLAlchemyError: If there is an error during the database operation.
    """
    existing_profile = get_model_by_pk_or_abort(db, Seeker, seeker_id)
    try:
        updated_profile = seeker_schema.load(
            request.get_json(), instance=existing_profile
        )
        db.session.commit()
        return seeker_schema.dump(updated_profile), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
