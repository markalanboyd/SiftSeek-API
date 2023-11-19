def test_seeker_delete_profile_success(client, profile_endpoint):
    response = client.delete(profile_endpoint)
    assert response.status_code == 202


def test_seeker_delete_profile_failure(client, invalid_profile_endpoint):
    response = client.delete(invalid_profile_endpoint)
    assert response.status_code == 404
