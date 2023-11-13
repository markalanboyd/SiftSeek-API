from typing import Type, Dict, Any

from flask import abort
from sqlalchemy.orm import DeclarativeMeta

from siftseek.models.db import db


def get_model_by_id_or_abort(model: Type[DeclarativeMeta], id: int, code: int = 404):
    instance = db.session.get(model, id)
    if instance is None:
        abort(code)
    return instance


def get_filtered_many_or_abort(
    model: Type[DeclarativeMeta], filter_criteria: Dict[str, Any], code: int = 404
):
    instances = db.session.query(model).filter_by(**filter_criteria).all()
    if not instances:
        abort(code)
    return instances
