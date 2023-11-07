import pytest

from siftseek import create_app
from siftseek.models.seeker import Seeker
from siftseek.models.db import db as db_instance
from siftseek.tests.test_data import seeker_profile_data


@pytest.fixture(scope="function")
def app():
    _app = create_app("test")
    with _app.app_context():
        db_instance.create_all()
        yield _app
        db_instance.session.remove()
        db_instance.drop_all()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def session(app):
    db_instance.session.begin()
    yield db_instance.session
    db_instance.session.rollback()
    db_instance.session.remove()


@pytest.fixture(scope="function")
def test_seeker_profile(session):
    new_seeker = Seeker(**seeker_profile_data.passing)
    session.add(new_seeker)
    session.commit()
    yield new_seeker
    session.delete(new_seeker)
    session.commit()
