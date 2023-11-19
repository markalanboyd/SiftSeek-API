def test_seeker_get_profile_success(client, profile_endpoint):
    get_response = client.get(profile_endpoint)
    assert get_response.status_code == 200


def test_seeker_get_profile_failure(client, invalid_profile_endpoint):
    get_response = client.get(invalid_profile_endpoint)
    assert get_response.status_code == 404
