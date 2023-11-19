from flask import Response, jsonify

from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import get_job_apps_by_seeker_id_or_404
from siftseek.models.job_application import JobApplication
from siftseek.schemas.job_application_schema import application_schema


@seeker.get("/application/<int:seeker_id>")
def get_all_applications(seeker_id: int) -> tuple[Response, int]:
    """
    Retrieves all the applications for a specific job seeker.

    #TODO Add: More flexible search parameters
    This method should be made more flexible by queries for X number of
    applications, within a date range, matching a status, and so on.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): A list of applications in JSON format.
            - (int): HTTP status code. 200 if successful, 404 if no instances found.

    Raises:
        HTTPException: If no instances are found, aborts with a 404 error.
        SQLAlchemyError: If there is an error during the database operation.
    """
    applications = get_job_apps_by_seeker_id_or_404(seeker_id)
    application_data = application_schema.dump(applications, many=True)
    return jsonify(application_data), 200
