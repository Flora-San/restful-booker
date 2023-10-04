# Test case to update an existing resource
import requests

# from helpers.api_helpers import BASE_URL

BASE_URL = "https://restful-booker.herokuapp.com"


def test_update_resource():
    resource_id = 1  # Replace with an existing resource ID
    endpoint = f"{BASE_URL}/api/resource/{resource_id}"
    updated_data = {
        "name": "Updated Resource Name"
    }
    response = requests.put(endpoint, json=updated_data)
    assert response.status_code == 200  # Assuming 200 indicates successful resource update

    # Verify that the resource has been updated by retrieving it again and comparing attributes
    updated_response = requests.get(endpoint)
    assert updated_response.status_code == 200
    assert updated_response.json()["name"] == updated_data["name"]
