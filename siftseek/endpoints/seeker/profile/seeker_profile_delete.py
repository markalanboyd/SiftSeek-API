from datetime import datetime

from flask import Response, jsonify

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_model_by_pk_or_404


@seeker.delete("/profile/<int:seeker_id>")
def mark_for_deletion(seeker_id: int) -> tuple[Response, int]:
    """
    Marks a profile for deletion. Actual deletion is handled by a chron job in
    siftseek.tasks.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): Response message.
            - (int): HTTP status code. 202 (accepted for processing) if successful,
            409 (conflict with current state of resource) if account has already
            been marked for deletion.

    Raises:
        HTTPException: If no instance is found, aborts with a 404 error.
        SQLAlchemyError: If there is an error during the database operation.
    """
    existing_profile = db.get_or_404(Seeker, seeker_id)
    if existing_profile.marked_for_deletion == True:
        deleted_at = existing_profile.deleted_at
        return (
            jsonify(
                {
                    "message": f"This account has already been marked for deletion. Deleted at {deleted_at}"
                }
            ),
            409,
        )
    existing_profile.marked_for_deletion = True
    existing_profile.deleted_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "The account has be marked for deletion."}), 202
