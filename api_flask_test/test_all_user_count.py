import requests
from utils.api_utils import get_api_data
from utils.config_reader import get_flask_app

base_uri = get_flask_app()
url_path = "allusercount"

#testing api all user count for status 200

def test_get_all_user_count():
    url = base_uri + url_path
    header = {'accept': 'application/json'}
    get_data = get_api_data(url, header)
    assert get_data.status_code == 200

def test_get_all_user_count_status_406():
    url = base_uri + url_path
    get_data = get_api_data(url)
    assert get_data.status_code == 406
