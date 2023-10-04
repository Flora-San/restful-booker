import pytest
import requests

# from helpers.api_helpers import BASE_URL
# Define the base URL for the Restful Booker API

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to create a token
def test_create_token():
    # Define the endpoint for authentication
    auth_endpoint = f"{BASE_URL}/auth"

    # Define the payload (username and password) for authentication
    auth_data = {
        "username": "admin",
        "password": "password123"
    }

    # Make a POST request to the authentication endpoint
    response = requests.post(auth_endpoint, json=auth_data)

    # Assert the response status code (200 indicates success)
    assert response.status_code == 200

    # Assert that the response contains a token
    assert "token" in response.json()


if __name__ == "__main__":
    pytest.main(["-v", "your_test_file.py"])
