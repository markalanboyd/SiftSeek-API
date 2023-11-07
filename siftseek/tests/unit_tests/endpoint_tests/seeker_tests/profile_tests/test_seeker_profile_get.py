def test_seeker_get_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"
    get_response = client.get(url)
    assert get_response.status_code == 200
