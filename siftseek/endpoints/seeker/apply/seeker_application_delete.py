from flask import Response, jsonify, request

from siftseek.endpoints.seeker import seeker
from siftseek.endpoints.helpers.query_helpers import (
    get_filtered_job_apps_by_seeker_id_or_404,
)
from siftseek.models.db import db


@seeker.delete("/application/<int:seeker_id>")
def delete_job_applications(seeker_id: int) -> tuple[Response, int]:
    """
    Deletes one or more job applications by job application id passed as a
    query parameter.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        tuple[Response, int]: A tuple containing:
            - (Response): A list of applications in JSON format.
            - (int): HTTP status code. 200 if successful, 404 if no instances found.

    Raises:
        HTTPException:
            - If no IDs are provided, aborts with a 400 error.
            - If IDs are malformed, aborts with a 400 error.
            - If no instances are found, aborts and raises a 404 error.
        SQLAlchemyError: If there is an error during the database operation.
    """
    job_apps_to_delete_ids = request.args.get("ids")
    if not job_apps_to_delete_ids:
        return jsonify(message="No job application IDs provided"), 400
    try:
        ids_to_delete = [int(id) for id in job_apps_to_delete_ids.split(",")]
    except ValueError:
        return jsonify(message="Invalid job application IDs provided."), 400
    job_applications = get_filtered_job_apps_by_seeker_id_or_404(
        seeker_id, ids_to_delete
    )
    for job_application in job_applications:
        db.session.delete(job_application)
    db.session.commit()
    return jsonify(message="Application(s) deleted successfully"), 200
