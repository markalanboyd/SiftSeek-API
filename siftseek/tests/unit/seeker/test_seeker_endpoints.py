import requests

from siftseek.tests.unit.seeker import seeker_endpoints_data as test_data


URL = "http://127.0.0.1:5000/"


def test_seeker_post_profile():
    url = URL + "seeker/profile"
    data = test_data.passing
    response = requests.post(url, json=data)
    assert response.status_code == 201


def test_seeker_get_profile():
    url = URL + "seeker/profile/1"
    response = requests.get(url)
    assert response.status_code == 200


def test_seeker_put_profile():
    url = URL + "seeker/profile/1"
    data = test_data.passing
    response = requests.put(url, json=data)
    assert response.status_code == 200


def test_seeker_patch_profile():
    url = URL + "seeker/profile/1"
    data = test_data.patch_passing
    response = requests.patch(url, json=data)
    assert response.status_code == 200


def test_seeker_delete_profile():
    url = URL + "seeker/profile/1"
    response = requests.delete(url)
    assert response.status_code == 202
