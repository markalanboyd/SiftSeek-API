def test_seeker_get_profile(client, profile_endpoint):
    get_response = client.get(profile_endpoint)
    assert get_response.status_code == 200
