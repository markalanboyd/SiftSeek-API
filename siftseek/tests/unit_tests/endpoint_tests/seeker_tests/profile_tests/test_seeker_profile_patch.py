from siftseek.tests.test_data import seeker_profile_data as test_data


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
