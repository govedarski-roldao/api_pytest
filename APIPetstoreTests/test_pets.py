from utils.my_utils import get_api_data, put_data
import random
from utils.my_config_parser import get_pet_url_api

base_uri = get_pet_url_api()
pet_id = str(random.randint(250002, 260002))


def test_get_pet_by_id():
    pet_data, res_status, time_taken = get_api_data(base_uri + "100")
    print(time_taken)
    assert pet_data["id"] == 100
    assert res_status == 200


# test updating a pet
def test_updating_pet():
    payload = {
        "id": 100,
        "name": "Pterolord",
        "status": "available"
    }
    print(base_uri)
    data, res_status, time_taken = put_data(base_uri, payload)
    print(data)
    assert data['id'] == 100

#