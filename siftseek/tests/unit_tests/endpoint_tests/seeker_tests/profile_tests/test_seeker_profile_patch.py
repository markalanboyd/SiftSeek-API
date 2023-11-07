def test_seeker_patch_profile(client, profile_endpoint, profile_passing_patch):
    # Make a PATCH request
    patch_response = client.patch(profile_endpoint, json=profile_passing_patch)
    assert patch_response.status_code == 200

    # Verify data matches
    updated_data = patch_response.get_json()
    for key, value in profile_passing_patch.items():
        assert updated_data[key] == value
