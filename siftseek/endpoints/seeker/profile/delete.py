from datetime import datetime

from flask import jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_model_by_id_or_abort


@seeker.delete("/profile/<int:id>")
def mark_for_deletion(id):
    existing_profile = get_model_by_id_or_abort(Seeker, id)
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
    try:
        existing_profile.marked_for_deletion = True
        existing_profile.deleted_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "The account has be marked for deletion."}), 202
    except ValidationError as e:
        db.session.rollback()
        return (
            jsonify(
                {"message": "Failed to mark account for deletion", "error": str(e)}
            ),
            500,
        )
