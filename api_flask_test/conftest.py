from utils.file_utils import get_json_from_file
from utils.api_utils import post_api_data
from utils.config_reader import get_flask_app
import pytest

login_json_file = "login_valid.json"
baseURI = get_flask_app()

login_url_path = "login"
users_url_path = "users"

@pytest.fixture()
def get_token():
    login_url = baseURI + login_url_path
    payload = get_json_from_file(login_json_file)
    resp = post_api_data(login_url, payload)
    token = resp.json()["token"]
    print(token)
    yield token