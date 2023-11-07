def test_seeker_put_profile_success(client, profile_endpoint, profile_passing_profile):
    put_response = client.put(profile_endpoint, json=profile_passing_profile)
    assert put_response.status_code == 200


def test_seeker_put_profile_failure(client, profile_endpoint, profile_failing_profile):
    put_response = client.put(profile_endpoint, json=profile_failing_profile)
    assert put_response.status_code == 400


def test_seeker_put_profile_persistence(
    client, profile_endpoint, profile_passing_profile
):
    client.put(profile_endpoint, json=profile_passing_profile)
    get_response = client.get(profile_endpoint)
    assert get_response.status_code == 200

    profile_after_put = get_response.get_json()
    for key, value in profile_passing_profile.items():
        assert profile_after_put[key] == value


def test_seeker_put_profile_idempotence(
    client, profile_endpoint, profile_passing_profile
):
    first_response = client.put(profile_endpoint, json=profile_passing_profile)
    assert first_response.status_code == 200

    second_response = client.put(profile_endpoint, json=profile_passing_profile)
    assert second_response.status_code == 200
