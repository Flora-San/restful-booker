import pytest
import requests

# Define the base URL for the Restful Booker API
BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to ping the "Ping - HealthCheck" endpoint and check API health
def test_ping_healthcheck():
    endpoint = f"{BASE_URL}/ping"
    response = requests.get(endpoint)

    # Assert the response status code (200 indicates a successful ping)
    assert response.status_code == 201

    # Assert that the response contains a specific message indicating API health
    response_json = response.json()
    assert "status" in response_json
    assert response_json["status"] == "Up"


if __name__ == "__main__":
    pytest.main(["-v", "your_test_file.py"])
