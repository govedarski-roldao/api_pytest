import requests, json, pytest
import random

base_uri = "https://petstore.swagger.io/v2/pet/"
pet_id = str(random.randint(250002, 260002))


@pytest.fixture
def pet_response():
    url = base_uri + pet_id
    headers = {"Content-Type": "application/json"}
    print("Resquest URL: ", url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    return data


# test valid response or response is not empty
def test_get_pet_by_id_response(pet_response):
    print(json.dumps(pet_response, indent=4, sort_keys=True))
    assert len(pet_response) > 0, "empty response"


# testing response body for "ID" key
def test_get_pet_by_id_id_not_added(pet_response):
    assert pet_response['message'] == "Pet not found"


# test adding new pet to store
def test_add_pet():
    url = base_uri
    headers = {"Content-Type": "application/json"}
    pet_data = {"id": int(pet_id),
                "name": "Petmotherfoca",
                "status": "zombie mode"}
    print(pet_id)
    response = requests.post(url, json=pet_data, headers=headers, verify=False)
    assert response.status_code == 200
    assert response.json()["id"] == int(pet_id)


def test_get_pet_by_id_present(pet_response):
    assert pet_response['id'] == int(pet_id)


def test_delete_pet_by_id():
    url = base_uri + pet_id
    response = requests.delete(url, verify=False)
    assert response.status_code == 200


def test_get_pet_by_id_id_deleted(pet_response):
    assert pet_response['message'] == "Pet not found"
