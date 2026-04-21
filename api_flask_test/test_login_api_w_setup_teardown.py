import pytest
from utils.api_utils import post_api_data
from utils.file_utils import get_json_from_file
from utils.my_config_parser import get_flask_app_base_url
import random

base_uri = get_flask_app_base_url()
reg_url_path = "register"
login_url_path = "login"
del_url_path
register_json_file = "register_api_valid.json"
rand_num = random.randint(0, 1000)
email = "automateuser@auto" + str(rand_num)
password = "1234"


@pytest.fixture
def reg_user():
    payload = get_payload_dict_regapi(email, password)
    regurl = base_uri + reg_url_path
    reg_response = post_api_data(regurl, payload)
    assert reg_response.status_code == 201
    assert reg_response.json()["id"]
    data = reg_response.json()
    yield data  ##anything after this stmt, will run as part of teardown, or after the test function is executed.
    del

def test_login_correct_create_creds(reg_user):
    payload = get_payload_dict_regapi(email, password)
    url = base_uri + login_url_path
    reg_response = post_api_data(url, payload)
    assert reg_response.status_code == 200


def test_login_empty_password(reg_user):
    payload = get_payload_dict_regapi(email, "")
    url = base_uri + login_url_path
    reg_response = post_api_data(url, payload)
    assert reg_response.status_code == 401


def get_payload_dict_regapi(email=None, pwd=None):
    payload = get_json_from_file(register_json_file)
    payload["email"] = email
    payload["password"] = pwd
    return payload
