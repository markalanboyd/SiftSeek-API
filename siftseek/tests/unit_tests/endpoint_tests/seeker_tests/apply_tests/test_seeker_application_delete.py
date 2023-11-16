def test_seeker_delete_applications_success(
    client,
    test_seeker_profile,
    apply_endpoint,
    application_data_passing,
    job_apps_to_delete,
):
    application_data_passing["seeker_id"] = test_seeker_profile.id
    response = client.post(apply_endpoint, json=application_data_passing)
    assert response.status_code == 201

    delete_response = client.delete(f"{apply_endpoint}?ids={job_apps_to_delete}")

    assert delete_response.status_code == 200
