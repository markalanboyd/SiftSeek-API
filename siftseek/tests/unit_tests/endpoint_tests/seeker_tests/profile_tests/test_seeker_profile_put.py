def test_seeker_put_profile_success(client, profile_endpoint, profile_passing_profile):
    endpoint = profile_endpoint
    passing_profile = profile_passing_profile

    # Make a PUT request
    put_response = client.put(endpoint, json=passing_profile)
    assert put_response.status_code == 200


def test_seeker_put_profile_failure(client, profile_endpoint, profile_failing_profile):
    endpoint = profile_endpoint
    failing_profile = profile_failing_profile

    put_response = client.put(endpoint, json=failing_profile)
    assert put_response.status_code == 400


def test_seeker_put_profile_persistence(
    client, profile_endpoint, profile_passing_profile
):
    endpoint = profile_endpoint
    passing_profile = profile_passing_profile

    # Verify data matches
    client.put(endpoint, json=passing_profile)
    get_response = client.get(endpoint)
    assert get_response.status_code == 200

    profile_after_put = get_response.get_json()
    for key, value in passing_profile.items():
        assert profile_after_put[key] == value


def test_seeker_put_profile_idempotence(
    client, profile_endpoint, profile_passing_profile
):
    endpoint = profile_endpoint
    passing_profile = profile_passing_profile

    first_response = client.put(endpoint, json=passing_profile)
    assert first_response.status_code == 200

    second_response = client.put(endpoint, json=passing_profile)
    assert second_response.status_code == 200
