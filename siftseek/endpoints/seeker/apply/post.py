from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.endpoints.seeker import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.post("/apply")
def apply_for_job():
    pass
