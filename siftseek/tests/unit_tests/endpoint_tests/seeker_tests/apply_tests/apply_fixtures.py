import pytest

from siftseek.tests.test_data import application_data


@pytest.fixture(scope="function")
def apply_endpoint(test_seeker_profile):
    return f"/seeker/apply/{test_seeker_profile.id}"


@pytest.fixture(scope="function")
def invalid_apply_endpoint():
    return f"/seeker/apply/0"


@pytest.fixture(scope="function")
def application_data_passing():
    return application_data.passing


@pytest.fixture(scope="function")
def application_data_failing():
    return application_data.failing
