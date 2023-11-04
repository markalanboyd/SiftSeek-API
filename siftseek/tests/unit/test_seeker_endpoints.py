import pytest
import requests

from siftseek import create_app
from siftseek.models.db import db as _db

URL = "http://127.0.0.1:5000/"


@pytest.fixture(scope="function")
def session(db):
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session  # this is where the testing happens

    session.remove()
    transaction.rollback()
    connection.close()


def test_seeker_post_profile(session):
    url = URL + "seeker/profile"
    data = {
        "username": "alexsmith",
        "first_name": "Alex",
        "last_name": "Smith",
        "contact_email": "alex.smith@example.com",
        "work_phone": "+1-212-555-1234",
        "work_phone_ext": "200",
        "cellphone": "+1-917-555-5678",
        "address": "456 Oak Lane",
        "city": "New York",
        "profile_pic_url": "http://example.com/images/alex_profile.jpg",
        "resume_url": "http://example.com/resumes/alex_resume.pdf",
        "linkedin_url": "http://linkedin.com/in/alexsmithprofessional",
        "portfolio_url": "http://alexsmithportfolio.com",
        "summary": "Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.",
        "education_level_id": 4,
        "remote_option": True,
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    # No need to clean up, as the session will be rolled back


def test_seeker_get_profile():
    url = URL + "seeker/profile/1"
    response = requests.get(url)
    assert response.status_code == 200
