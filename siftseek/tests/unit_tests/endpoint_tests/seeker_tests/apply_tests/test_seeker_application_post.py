def test_seeker_post_application_success(
    client, test_seeker_profile, apply_endpoint, application_data_passing
):
    application_data_passing["seeker_id"] = test_seeker_profile.id
    response = client.post(
        f"{apply_endpoint}/{test_seeker_profile.id}", json=application_data_passing
    )
    assert response.status_code == 201


def test_seeker_post_application_failure(
    client, test_seeker_profile, apply_endpoint, application_data_failing
):
    response = client.post(
        f"{apply_endpoint}/{test_seeker_profile.id}", json=application_data_failing
    )
    assert response.status_code == 400
