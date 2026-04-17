from utils.file_utils import get_csv_from_file
from utils.api_utils import get_api_data, post_api_data
from utils.config_reader import get_flask_app

base_uri = get_flask_app()
data_file = get_csv_from_file("register_api_data.csv")
url_path = "register"

def test_data_driven():
    url = base_uri + url_path
    payload_list = data_file
    print(url, payload_list)
    for payload in payload_list:
        resp = post_api_data(url, payload)
        assert resp.status_code == 201