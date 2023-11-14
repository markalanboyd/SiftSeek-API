from flask import Response, request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.job_application_schema import application_schema


@seeker.post("/apply/<int:seeker_id>")
def apply_for_job(seeker_id: int) -> tuple[Response, int]:
    """
    Posts an application for a specific job seeker.

    #TODO Add: Connection to job posting
    This route and model does not yet connect with a job posting. Once
    the Company endpoint has been completed, I will come back and connect
    these models.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): The application to be posted.
            - (int): HTTP status code. 200 if successful, 400 for validation errors.

    Raises:
        ValidationError: If `new_application` fails to validate with the marshmallow schema.
        SQLAlchemyError: If there is an error during the database operation.
    """
    try:
        application_data = request.get_json()
        application_data["seeker_id"] = seeker_id

        new_application = application_schema.load(application_data)
        db.session.add(new_application)
        db.session.commit()

        return application_schema.dump(new_application), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
