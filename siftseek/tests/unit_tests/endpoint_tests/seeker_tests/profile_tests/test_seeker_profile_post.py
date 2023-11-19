def test_seeker_post_profile_success(client, seeker_passing_profile):
    endpoint = "/seeker/profile"
    post_response = client.post(endpoint, json=seeker_passing_profile)
    assert post_response.status_code == 201


def test_seeker_post_profile_success(client, seeker_failing_profile):
    endpoint = "/seeker/profile"
    post_response = client.post(endpoint, json=seeker_failing_profile)
    assert post_response.status_code == 400
