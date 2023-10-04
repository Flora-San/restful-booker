import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to get a booking by ID
def test_get_booking():
    booking_id = 1  # Replace with an existing booking ID
    endpoint = f"{BASE_URL}/booking/{booking_id}"
    response = requests.get(endpoint)
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", "test_get_booking.py"])
