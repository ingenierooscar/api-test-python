import json
import requests


url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
    "id": 123456781234,
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

headers = {
    'Content-Type': 'application/json'
}


response = requests.post(url, headers=headers, data=payload)

print(response.status_code)
