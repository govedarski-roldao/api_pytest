import pytest
from utils.file_utils import get_csv_from_file
from utils.api_utils import get_api_data, post_api_data, delete_api_data
from utils.config_reader import get_flask_app

base_uri = get_flask_app()
data_file = get_csv_from_file("register_api_data.csv")
url_path_register = "register"
url_path_delete = "delete"
url_register = base_uri + url_path_register
url_delete = base_uri + url_path_delete
url_path_login = "login"
url_login = base_uri + url_path_login


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
