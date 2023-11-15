from flask import Response, jsonify, request
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.job_application import JobApplication
from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_model_by_pk_or_404
from siftseek.schemas.job_application_schema import application_schema


@seeker.put("/apply/<int:seeker_id>")
def update_job_application(seeker_id: int) -> tuple[Response, int]:
    """
    Updates a job application for a specific job seeker.

    #TODO Implement authentication to use seeker_id
    Right now, the seeker_id is unused, but I might need it in the future for
    authentication purposes.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): The application to be updated.
            - (int): HTTP status code. 200 if successful, 400 for validation errors.

    Raises:
        HTTPException: If the ID provided is not an integer, aborts with a 400 error.
        ValidationError: If `updated_job_application` fails to validate with
            the marshmallow schema.
        SQLAlchemyError: If there is an error during the database operation.
    """
    job_app_to_update_id = request.args.get("id")
    try:
        job_application_id = int(job_app_to_update_id)
    except ValueError:
        return jsonify(message="ID provided is not an integer."), 400

    existing_job_application = get_model_by_pk_or_404(
        JobApplication, job_application_id
    )
    try:
        updated_job_app_data = request.get_json()

        updated_job_application = application_schema.load(
            updated_job_app_data, instance=existing_job_application
        )
        db.session.commit()
        return application_schema.dump(updated_job_application), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
