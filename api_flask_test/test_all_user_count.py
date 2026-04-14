import requests
from utils.api_utils import get_api_data
from utils.config_reader import get_flask_app
import pytest

base_uri = get_flask_app()
url_path = "allusercount"
url = base_uri + url_path
test_data = [
    ("application/json", 200),
    ("application/xml", 406),
    ("multipart/mixed", 406),
    ("text/plain", 406)
]


@pytest.mark.parametrize("type, status_code", test_data)
def test_get_all_user_count_status_codes(type, status_code):
    header = {'accept': type}
    response = get_api_data(url, header)
    assert response.status_code == status_code


# testing api all user count for status 200
@pytest.mark.parametrize("status_code", [200, 406])
def test_get_all_users_status(status_code):
    header = {'accept': 'application/json'}
    if status_code == 200:
        get_data = get_api_data(url, header)
    else:
        get_data = get_api_data(url)
    assert get_data.status_code == status_code


# testing api all user count for status 200
def test_get_all_user_count():
    header = {'accept': 'application/json'}
    get_data = get_api_data(url, header)
    assert get_data.status_code == 200


def test_get_all_user_count_status_406():
    get_data = get_api_data(url)
    assert get_data.status_code == 406


def test_get_all_user_count_body():
    header = {'accept': 'application/json'}
    get_data = get_api_data(url, header)
    data = get_data.json()
    assert data['count'] == 4
    assert data['status']
    assert data['status']['message'] == 'success'


def test_get_all_user_count_time_taken():
    header = {'accept': 'application/json'}
    get_data = get_api_data(url, header)
    print(get_data.elapsed.total_seconds())
    assert (get_data.elapsed.total_seconds()) < 1
