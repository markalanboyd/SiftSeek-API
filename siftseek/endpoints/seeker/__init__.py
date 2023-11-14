"""
The siftseek.endpoints.seeker __init__.py file creates the seeker blueprint and
imports its routes.
"""

from flask import Blueprint

seeker = Blueprint("seeker", __name__)

from siftseek.endpoints.seeker.profile import (
    seeker_profile_get,
    seeker_profile_delete,
    seeker_profile_patch,
    seeker_profile_post,
    seeker_profile_put,
)

from siftseek.endpoints.seeker.apply import seeker_apply_post, seeker_apply_get
