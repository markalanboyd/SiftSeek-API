"""
query_helpers.py provides helper functions for querying the database in the SiftSeek
application.

Each helper supports a custom error code for future development.
"""

from typing import Type, Any, List, Optional, TypeAlias

from flask import abort
from sqlalchemy import and_

from siftseek.models.db import db, Base
from siftseek.models.seeker import Seeker
from siftseek.models.job_application import JobApplication

# TODO Set up TypeAlias for Base


def get_model_by_pk_or_404(model: Type[Base], pk: Any) -> Optional[Base]:
    """
    Tries to return a model from a database using its primary key. If no
    instance is found, aborts with a 404.

    Args:
        model (Type[Base]): The model being searched for.
        pk (Any): The primary key value used to identify the model instance.
        error_code (int, optional): The HTTP error code. Defaults to 404.

    Returns:
        Optional[Base]: The model searched for or None if none found.

    Raises:
        HTTPException: If no instances are found, aborts and raises 404.
    """
    instance = db.session.get(model, pk)
    if not instance:
        abort(404)
    return instance


def get_job_apps_by_seeker_id_or_404(seeker_id: int) -> Optional[list[Base]]:
    """
    Tries to return all job applications by a seeker. If no instances are found,
    aborts with a 404.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        Optional[list[Base]]: A list of all the applications or None if none found.

    Raises:
        HTTPException: If no instances are found, aborts and raises 404.
        SQLAlchemyError: If there is an error during the database operation.
    """
    instances = (
        db.session.query(JobApplication)
        .filter(JobApplication.seeker_id == seeker_id)
        .all()
    )
    if not instances:
        abort(404)
    return instances


def get_filtered_job_apps_by_seeker_id_or_404(
    seeker_id: int,
    job_application_ids: List[int],
) -> Optional[List[Base]]:
    """
    Tries to return a list of job applications by a seeker filtered by their id.
    If no instances are found, aborts with a 404.

    Args:
        seeker_id (int): The primary key ID of the seeker.

    Returns:
        Optional[list[Base]]: A list of all the applications or None if none found.

    Raises:
        HTTPException: If no instances are found, aborts and raises 404.
        SQLAlchemyError: If there is an error during the database operation.
    """
    instances = (
        db.session.query(JobApplication)
        .filter(
            and_(
                JobApplication.seeker_id == seeker_id,
                JobApplication.id.in_(job_application_ids),
            )
        )
        .all()
    )
    if not instances:
        abort(404)
    return instances
