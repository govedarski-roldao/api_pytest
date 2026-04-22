import pytest
from utils.api_utils import post_api_data, new_del_api
from utils.file_utils import get_json_from_file
from utils.my_config_parser import get_flask_app_base_url
import random

base_uri = get_flask_app_base_url()
reg_url_path = "register"
login_url_path = "login"
del_url_path = "delete"
register_json_file = "register_api_valid.json"
rand_num = random.randint(0, 1000)


# email = "automateuser@auto" + str(rand_num)
# password = "1234"


def generate_worker():
    rand_num = random.randint(0, 1000)
    email = "automateuser@auto" + str(rand_num)
    password = random.randint(1111, 9999)
    return email, str(password)


@pytest.fixture
def reg_user():
    ## test setup

    email, password = generate_worker()
    payload = get_payload_dict_regapi(email, password)
    regurl = base_uri + reg_url_path
    reg_response = post_api_data(regurl, payload)
    assert reg_response.status_code == 201
    assert reg_response.json()["id"]
    data = reg_response.json()
    yield {
        "email": email,
        "password": password,
        "id": data["id"]
    }  ##anything after this stmt, will run as part of teardown, or after the test function is executed.

    ## test teardown

    del_url = base_uri + del_url_path
    login_url = base_uri + login_url_path
    login_resp = post_api_data(login_url, payload)
    token = login_resp.json()["token"]
    headers = {"x-access-token": token}
    payload = {"id": reg_response.json()["id"]}
    del_resp = new_del_api(del_url, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()["id"] == reg_response.json()["id"]


def test_login_correct_create_creds(reg_user):
    print("reg_user:", reg_user)
    payload = {
        "email": reg_user["email"],
        "password": reg_user["password"]
    }
    url = base_uri + login_url_path
    reg_response = post_api_data(url, payload)
    assert reg_response.status_code == 200


def test_login_empty_password(reg_user):
    payload = {
        "email": reg_user["email"],
        "password": ""
    }
    url = base_uri + login_url_path
    reg_response = post_api_data(url, payload)
    assert reg_response.status_code == 401


def get_payload_dict_regapi(email=None, pwd=None):
    payload = get_json_from_file(register_json_file)
    payload["email"] = email
    payload["password"] = pwd
    return payload
