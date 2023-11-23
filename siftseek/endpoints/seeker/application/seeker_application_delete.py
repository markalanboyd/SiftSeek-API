from flask import Response, jsonify

from siftseek.endpoints.seeker import seeker
from siftseek.models.db import db
from siftseek.models.job_application import JobApplication


@seeker.delete("/application/<int:application_id>")
def delete_job_applications(application_id: int) -> tuple[Response, int]:
    """
    Deletes one or more job applications by job application id passed as a
    query parameter.

    Args:
        application_id (int): The primary key ID of the job application.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): A list of applications in JSON format.
            - (int): HTTP status code. 200 if successful, 404 if no instances found.

    Raises:
        HTTPException:
            - If no instances are found, aborts and raises a 404 error.
        SQLAlchemyError: If there is an error during the database operation.
    """

    job_application = db.get_or_404(JobApplication, application_id)
    db.session.delete(job_application)
    db.session.commit()
    return jsonify(message="Application deleted successfully"), 200
