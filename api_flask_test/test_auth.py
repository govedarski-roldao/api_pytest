from utils.file_utils import get_json_from_file
from utils.api_utils import get_api_data, post_api_data
from utils.config_reader import get_flask_app

login_json_file = "login_valid.json"

baseURI = get_flask_app()
login_url_path = "login"
users_url_path = "users"


def test_get_users_demo():
    # first login with existing user
    url = baseURI + login_url_path
    payload = get_json_from_file(login_json_file)
    resp = post_api_data(url, payload)
    print(resp.json()["token"])
    token = resp.json()["token"]
    userURL = baseURI + users_url_path
    headers = {"x-access-token": token}
    r_users = get_api_data(userURL, headers)
    print(r_users.status_code)
    assert r_users.status_code == 200
