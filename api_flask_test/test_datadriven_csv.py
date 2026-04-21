import pytest
from utils.file_utils import get_csv_from_file, get_data_as_tuple
from utils.api_utils import get_api_data, post_api_data, delete_api_data
from utils.my_config_parser import get_flask_app_base_url

base_uri = get_flask_app_base_url()
data_file = get_csv_from_file("register_api_data.csv")
url_path_register = "register"
url_path_delete = "delete"
url_register = base_uri + url_path_register
url_delete = base_uri + url_path_delete
url_path_login = "login"
url_login = base_uri + url_path_login
data_file_with_status = "register_api_data_with_status.csv"


def test_data_driven():
    payload_list = data_file
    print(url_register, payload_list)
    for payload in payload_list:
        resp = post_api_data(url_register, payload)
        assert resp.status_code == 201


@pytest.mark.parametrize("line", data_file)
def test_driven_param(line):
    print(line)

    # REGISTER
    resp = post_api_data(url_register, line)
    assert resp.status_code == 201

    user = resp.json()["id"]
    print("id:", user)

    # LOGIN (geralmente só email e password)
    login_payload = {
        "email": line["email"],
        "password": line["password"]
    }

    login_resp = post_api_data(url_login, login_payload)
    token = login_resp.json()["token"]

    # DELETE
    delete_status = delete_api_data(url_delete, user, token)

    assert delete_status.status_code == 200


get_data = get_data_as_tuple(data_file_with_status)


@pytest.mark.parametrize("input, resp_status", get_data)
def test_data_driven2(input, resp_status):
    url = base_uri + url_path_register
    keys = ["email", "password"]
    request_dict = dict(zip(keys, input))
    print("Request dict:", request_dict, resp_status)
    resp = post_api_data(url, request_dict)
    assert resp.status_code == int(resp_status)