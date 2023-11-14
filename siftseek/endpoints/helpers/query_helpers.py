"""
query_helpers.py provides helper functions for querying the database in the SiftSeek
application.

Each helper supports a custom error code for future development.
"""

from typing import Type, Dict, Any, List, Optional

from flask import abort
from flask_sqlalchemy import SQLAlchemy

from siftseek.models.db import Base


def get_model_by_pk_or_abort(
    db: SQLAlchemy, model: Type[Base], pk: Any, error_code: int = 404
) -> Optional[Base]:
    """
    Tries to return a model from a database using its primary key. If no
    instance is found, returns an HTTP resposne with the specified error.

    Args:
        db (SQLAlchemy): The SQLAlchemy database instance used for the query.
        model (Type[Base]): The model being searched for.
        pk (Any): The primary key value used to identify the model instance.
        error_code (int, optional): The HTTP error code. Defaults to 404.

    Returns:
        Optional[Base]: The model searched for or None if none found.

    Raises:
        HTTPException: If no instances are found, aborts the request and raises
        an HTTPException. Defaults to 404.
    """
    instance = db.session.get(model, pk)
    if not instance:
        abort(error_code)
    return instance


def get_models_filtered_or_abort(
    db: SQLAlchemy,
    model: Type[Base],
    filter_criteria: Dict[str, Any],
    error_code: int = 404,
) -> Optional[List[Base]]:
    """
    Returns a list of model instances from an SQLAlchemy database instance by
    the specified filter criteria.

    Args:
        db (SQLAlchemy): The SQLAlchemy database instance used for the query.
        model (Type[Base]): The model being searched for.
        filter_criteria (Dict[str, Any]): A dictionary of criteria to filter for.
        error_code (int, optional): The HTTP error code. Defaults to 404.

    Returns:
        Optional[List[Base]]: A list of the models searched for or None if none found.

    Raises:
        HTTPException: If no instances are found, aborts the request and raises
            an HTTPException. Defaults to 404.
    """
    instances = db.session.query(model).filter_by(**filter_criteria).all()
    if not instances:
        abort(error_code)
    return instances
