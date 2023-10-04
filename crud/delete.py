# Test case to delete an existing resource
import requests

# from helpers.api_helpers import BASE_URL
BASE_URL = "https://restful-booker.herokuapp.com"


def test_delete_resource():
    resource_id = 1  # Replace with an existing resource ID
    endpoint = f"{BASE_URL}/api/resource/{resource_id}"
    response = requests.delete(endpoint)
    assert response.status_code == 204  # Assuming 204 indicates successful resource deletion

    # Verify that the resource has been deleted by attempting to retrieve it again
    deleted_response = requests.get(endpoint)
    assert deleted_response.status_code == 404  # Assuming 404 indicates that the resource does not exist
