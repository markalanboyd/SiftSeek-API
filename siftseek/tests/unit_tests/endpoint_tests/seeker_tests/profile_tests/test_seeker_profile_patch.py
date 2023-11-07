def test_seeker_patch_profile_success(client, profile_endpoint, seeker_passing_patch):
    patch_response = client.patch(profile_endpoint, json=seeker_passing_patch)
    assert patch_response.status_code == 200


def test_seeker_patch_profile_failure(client, profile_endpoint, seeker_failing_patch):
    patch_response = client.patch(profile_endpoint, json=seeker_failing_patch)
    assert patch_response.status_code == 400


def test_seeker_patch_profile_persistence(
    client, profile_endpoint, seeker_passing_patch
):
    client.patch(profile_endpoint, json=seeker_passing_patch)
    get_response = client.get(profile_endpoint)
    assert get_response.status_code == 200

    profile_after_patch = get_response.get_json()
    for key, value in seeker_passing_patch.items():
        assert profile_after_patch[key] == value


def test_seeker_patch_profile_idempotence(
    client, profile_endpoint, seeker_passing_patch
):
    first_response = client.patch(profile_endpoint, json=seeker_passing_patch)
    assert first_response.status_code == 200
    second_response = client.patch(profile_endpoint, json=seeker_passing_patch)
    assert second_response.status_code == 200
