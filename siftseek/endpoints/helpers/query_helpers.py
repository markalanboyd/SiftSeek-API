from typing import Type

from flask import abort
from sqlalchemy.orm import DeclarativeMeta

from siftseek.models.db import db
from siftseek.models.seeker import Seeker


def get_or_abort(model: Type[DeclarativeMeta], id: int, code: int = 404):
    instance = db.session.get(model, id)
    if instance is None:
        abort(code)
    return instance
