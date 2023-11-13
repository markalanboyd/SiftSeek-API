from pprint import pprint


def test_seeker_post_application_success(
    client, test_seeker_profile, apply_endpoint, application_data_passing
):
    application_data_passing["seeker_id"] = test_seeker_profile.id
    response = client.post(apply_endpoint, json=application_data_passing)
    assert response.status_code == 201


def test_seeker_post_application_failure(
    client, apply_endpoint, application_data_failing
):
    response = client.post(apply_endpoint, json=application_data_failing)
    assert response.status_code == 400


def test_seeker_get_applications_success(
    client, test_seeker_profile, apply_endpoint, application_data_passing
):
    application_data_passing["seeker_id"] = test_seeker_profile.id
    response = client.post(apply_endpoint, json=application_data_passing)
    assert response.status_code == 201

    get_response = client.get(apply_endpoint)

    assert get_response.status_code == 200
