from flask import Response, jsonify

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.seeker_schema import seeker_schema


@seeker.get("/profile/<int:seeker_id>")
def get_profile(seeker_id: int) -> tuple[Response, int]:
    """
    Retrieves a seeker's profile by its primary key ID.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): The seeker's profile.
            - (int): HTTP status code. 200 if successful, 404 if account has
                already been marked for deletion.

    Raises:
        HTTPException: If no instance is found, aborts with a 404 error.
        SQLAlchemyError: If there is an error during the database operation.
    """
    seeker_profile = db.get_or_404(Seeker, seeker_id)
    return seeker_schema.jsonify(seeker_profile), 200
