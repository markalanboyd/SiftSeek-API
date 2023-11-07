from flask import Blueprint

seeker = Blueprint("seeker", __name__)

from .profile import get as profile_get
from .profile import delete as profile_delete
from .profile import patch as profile_patch
from .profile import post as profile_post
from .profile import put as profile_put

from .apply import post as apply_post
