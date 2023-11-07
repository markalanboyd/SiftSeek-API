from siftseek.tests.test_data import seeker_profile_data as test_data


def test_seeker_post_profile(client):
    url = "/seeker/profile"
    profile_data = test_data.passing
    post_response = client.post(url, json=profile_data)
    assert post_response.status_code == 201


def test_seeker_get_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"
    get_response = client.get(url)
    assert get_response.status_code == 200


def test_seeker_put_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"
    profile_data = test_data.passing

    # Make a PUT request
    put_response = client.put(url, json=profile_data)
    assert put_response.status_code == 200

    # Verify data matches
    updated_profile = put_response.get_json()
    for key, value in profile_data.items():
        assert updated_profile[key] == value

    # GET profile to verify change
    get_response = client.get(url)
    assert get_response.status_code == 200
    profile_after_put = get_response.get_json()
    for key, value in profile_data.items():
        assert profile_after_put[key] == value

    # Idempotence check
    second_response = client.put(url, json=profile_data)
    assert second_response.status_code == 200


def test_seeker_patch_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"
    patch_data = test_data.patch_passing

    # Make a PATCH request
    patch_response = client.patch(url, json=patch_data)
    assert patch_response.status_code == 200

    # Verify data matches
    updated_data = patch_response.get_json()
    for key, value in patch_data.items():
        assert updated_data[key] == value


def test_seeker_delete_profile(client, test_seeker_profile):
    url = f"/seeker/profile/{test_seeker_profile.id}"

    # Make a DELETE request
    response = client.delete(url)
    assert response.status_code == 202
