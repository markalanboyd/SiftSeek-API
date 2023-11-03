from . import seeker


@seeker.post("/profile")
def post_profile():
    return "Here we'll post the profile"


@seeker.get("/profile")
def get_profile():
    return "Seeker profile page"
