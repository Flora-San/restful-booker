import pytest
import requests
from helpers.api_helpers import BaseUrl

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to get booking IDs
def test_get_booking_ids():
    endpoint = f"{BASE_URL}/booking"
    response = requests.get(endpoint)
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", "test_get_booking_ids.py"])
