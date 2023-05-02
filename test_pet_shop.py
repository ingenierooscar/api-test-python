import requests
import json

ENDOINT = "https://petstore.swagger.io/v2/pet"


def test_list_pet_auth():
    list_pet_response = list_pet()
    assert list_pet_response.status_code == 200
    # print(list_pet_response.json())


def test_add_new_pet():
    add_new_pet_response = add_new_pet()
    assert add_new_pet_response.status_code == 200
    print(add_new_pet_response.json())


def test_find_pet_id():
    add_new_pet_response = add_new_pet()
    assert add_new_pet_response.status_code == 200
    data = add_new_pet_response.json()["id"]
    find_pet_id_response = find_pet_id(data)
    assert find_pet_id_response.status_code == 200


def list_pet():
    return requests.get(
        ENDOINT + "/findByStatus", params={"status": "available"})


def add_new_pet():
    payload = payload_pet()
    headers = {'Content-Type': 'application/json'}
    return requests.post(ENDOINT, headers=headers, data=payload)


def find_pet_id(pet_id):
    return requests.get(f"{ENDOINT}/{pet_id}")


def payload_pet():
    return json.dumps({
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    })
