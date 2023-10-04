# Test case to retrieve a resource by ID
import requests

# from helpers.api_helpers import BASE_URL

BASE_URL = "https://restful-booker.herokuapp.com"


def test_read_resource_by_id():
    resource_id = 1  # Replace with an existing resource ID
    endpoint = f"{BASE_URL}/api/resource/{resource_id}"
    response = requests.get(endpoint)
    assert response.status_code == 200  # Assuming 200 indicates successful resource retrieval
    assert "name" in response.json()  # Assuming the response includes a 'name' field

