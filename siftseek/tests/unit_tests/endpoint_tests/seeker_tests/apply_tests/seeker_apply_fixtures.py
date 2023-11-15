"""
This seeker_apply_fixtures.py file creates pytest fixtures for the seeker/apply endpoint.
"""

import pytest

from siftseek.tests.test_data import job_application_data


@pytest.fixture(scope="function")
def apply_endpoint(test_seeker_profile):
    return f"/seeker/apply/{test_seeker_profile.id}"


@pytest.fixture(scope="function")
def invalid_apply_endpoint():
    return f"/seeker/apply/0"


@pytest.fixture(scope="function")
def application_data_passing():
    return job_application_data.passing


@pytest.fixture(scope="function")
def application_data_failing():
    return job_application_data.failing


@pytest.fixture(scope="function")
def job_apps_to_delete():
    return job_application_data.applications_to_delete


@pytest.fixture(scope="function")
def application_put_data_passing():
    return job_application_data.put_passing
