from utils.my_utils import get_api_data
import random

base_uri = "https://petstore.swagger.io/v2/pet/"
pet_id = str(random.randint(250002, 260002))


def test_get_pet_by_id():
    pet_data, res_status, time_taken = get_api_data(base_uri + "100")
    print(time_taken)
    assert pet_data["id"] == 100
