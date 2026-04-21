from utils.api_utils import post_api_data
from utils.file_utils import get_json_from_file
from utils.my_config_parser import get_flask_app_base_url

base_uri = get_flask_app_base_url()
url_path = "register"
register_json_file = "register_api_valid.json"


# register_json_file = get_json_from_file("register_api_valid.json")
# testing register api with body from file
def test_register_api():
    url = base_uri + url_path
    payload = get_json_from_file(register_json_file)
    resp = post_api_data(url, payload)
    print(resp.json())
    assert resp.status_code == 201
