def test_seeker_delete_profile(client, profile_endpoint):
    response = client.delete(profile_endpoint)
    assert response.status_code == 202
