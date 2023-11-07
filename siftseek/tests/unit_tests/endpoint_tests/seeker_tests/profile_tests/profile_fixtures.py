import pytest

from siftseek.tests.test_data import seeker_profile_data


@pytest.fixture(scope="function")
def profile_endpoint(test_seeker_profile):
    return f"/seeker/profile/{test_seeker_profile.id}"


@pytest.fixture(scope="function")
def profile_passing_profile():
    return seeker_profile_data.passing


@pytest.fixture(scope="function")
def profile_failing_profile():
    return seeker_profile_data.failing


@pytest.fixture(scope="function")
def profile_passing_patch():
    return seeker_profile_data.patch_passing


@pytest.fixture(scope="function")
def profile_failing_patch():
    return seeker_profile_data.patch_failing
