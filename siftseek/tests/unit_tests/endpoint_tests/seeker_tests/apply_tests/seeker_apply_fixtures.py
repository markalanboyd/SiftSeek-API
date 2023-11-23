"""
This seeker_apply_fixtures.py file creates pytest fixtures for the seeker/apply endpoint.
"""

import pytest

from siftseek.tests.test_data import job_application_data


@pytest.fixture(scope="function")
def apply_endpoint(test_seeker_profile):
    return f"/seeker/application"


@pytest.fixture(scope="function")
def invalid_apply_endpoint():
    return f"/seeker/application/0"


@pytest.fixture(scope="function")
def application_data_passing():
    return job_application_data.passing


@pytest.fixture(scope="function")
def application_data_failing():
    return job_application_data.failing


@pytest.fixture(scope="function")
def job_app_to_delete():
    return job_application_data.application_to_delete


@pytest.fixture(scope="function")
def application_put_data_passing():
    return job_application_data.put_passing
