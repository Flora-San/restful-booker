import requests
from helpers.api_helpers import BaseUrl

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to create a new resource
def test_create_resource():
    endpoint = f"{BASE_URL}/api/resource"
    data = {
        "name": "New Resource",
        "description": "Description of the new resource"
    }
    response = requests.post(endpoint, json=data)
    assert response.status_code == 201  # Assuming 201 indicates successful resource creation
    assert "id" in response.json()  # Assuming the response includes an 'id' field

# You can add more assertions to verify the created resource's attributes
