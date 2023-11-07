from siftseek.tests.test_data import seeker_profile_data as test_data


def test_seeker_delete_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"

    # Make a DELETE request
    response = client.delete(url)
    assert response.status_code == 202
