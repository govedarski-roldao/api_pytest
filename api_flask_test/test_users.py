import json
from utils.api_utils import get_api_data
from utils.config_reader import get_flask_app

login_json_file = "login_valid.json"

baseURI = get_flask_app()
login_url_path = "login"
users_url_path = "users"


def test_get_users(get_token):
    token = get_token
    users_url = baseURI + users_url_path
    headers = {"x-access-token": token}
    resp = get_api_data(users_url, headers)
    print(json.dumps(resp.json(), indent=4))
    assert resp.json()["users"][0]["email"] == "admin@admin"
