def test_seeker_put_job_application_success(
    client,
    test_seeker_profile,
    apply_endpoint,
    application_data_passing,
    application_put_data_passing,
):
    application_data_passing["seeker_id"] = test_seeker_profile.id
    response = client.post(apply_endpoint, json=application_data_passing)
    assert response.status_code == 201

    put_response = client.put(
        f"{apply_endpoint}?id={test_seeker_profile.id}",
        json=application_put_data_passing,
    )

    assert put_response.status_code == 200
