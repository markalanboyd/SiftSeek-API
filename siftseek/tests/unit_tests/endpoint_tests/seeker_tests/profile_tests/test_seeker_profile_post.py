def test_seeker_post_profile_success(client, profile_passing_profile):
    endpoint = "/seeker/profile"
    passing_profile = profile_passing_profile
    post_response = client.post(endpoint, json=passing_profile)
    assert post_response.status_code == 201


def test_seeker_post_profile_success(client, profile_failing_profile):
    endpoint = "/seeker/profile"
    failing_profile = profile_failing_profile
    post_response = client.post(endpoint, json=failing_profile)
    assert post_response.status_code == 400
