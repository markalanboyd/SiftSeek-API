from datetime import datetime

from flask import request, jsonify, abort

from siftseek.models.db import db
from siftseek.models.seeker import Seeker
from . import seeker
from siftseek.schemas.SeekerSchema import seeker_schema


@seeker.post("/profile")
def post_profile():
    data = request.get_json()
    new_seeker = Seeker(
        # Metadata
        modified_at=datetime.utcnow(),
        # Personal Info
        username=data.get("username"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        contact_email=data.get("contact_email"),
        work_phone=data.get("work_phone"),
        work_phone_ext=data.get("work_phone_ext"),
        cellphone=data.get("cellphone"),
        address=data.get("address"),
        city=data.get("city"),
        # URLs
        resume_url=data.get("resume_url"),
        linkedin_url=data.get("linkedin_url"),
        portfolio_url=data.get("portfolio_url"),
        # Resume Info
        summary=data.get("summary"),
        education_level_id=data.get("education_level_id"),
        remote_option=data.get("remote_option"),
    )

    db.session.add(new_seeker)
    db.session.commit()

    return "Added to DB"


@seeker.get("/profile/<int:id>")
def get_profile(id):
    seeker_profile = Seeker.query.get_or_404(id)
    return seeker_schema.jsonify(seeker_profile)
