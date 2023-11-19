"""
This seeker_profile_fixtures.py file creates pytest fixtures for the seeker/profile endpoint.
"""

import pytest

from siftseek.tests.test_data import seeker_profile_data


@pytest.fixture(scope="function")
def profile_endpoint(test_seeker_profile):
    return f"/seeker/profile/{test_seeker_profile.id}"


@pytest.fixture(scope="function")
def invalid_profile_endpoint():
    return f"/seeker/profile/0"


@pytest.fixture(scope="function")
def seeker_passing_profile():
    return seeker_profile_data.passing


@pytest.fixture(scope="function")
def seeker_failing_profile():
    return seeker_profile_data.failing


@pytest.fixture(scope="function")
def seeker_passing_patch():
    return seeker_profile_data.patch_passing


@pytest.fixture(scope="function")
def seeker_failing_patch():
    return seeker_profile_data.patch_failing
