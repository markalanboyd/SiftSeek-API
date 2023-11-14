"""
This test module contains pytest fixtures for the SiftSeek application. 

It sets up fixtures for creating a Flask application context, a test client,
a database session, and a test seeker profile. These fixtures are used to facilitate
and simplify the testing of different components of the SiftSeek application,
especially the seeker-related endpoints and functionalities.

Fixtures:
    app: Creates a Flask application in a test configuration, setting up and 
        tearing down the database for each test function.
    client: Provides a test client for the Flask application, allowing for the
        simulation of HTTP requests to the application.
    session: Sets up and rolls back a database session for each test, ensuring
        data consistency and isolation between tests.
    test_seeker_profile: Creates and tears down a seeker profile in the database,
        providing a consistent test data set for seeker-related tests.

Each fixture is function-scoped, meaning it's created and destroyed for each test function, 
ensuring a clean state for every test.
"""


import pytest

from siftseek import create_app
from siftseek.models.seeker import Seeker
from siftseek.models.db import db as db_instance
from siftseek.tests.test_data import seeker_profile_data
from siftseek.tests.unit_tests.endpoint_tests.seeker_tests.profile_tests.seeker_profile_fixtures import *
from siftseek.tests.unit_tests.endpoint_tests.seeker_tests.apply_tests.seeker_apply_fixtures import *


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
def session():
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
