import pytest
import requests
import json

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to create a new booking
def test_create_booking():
    endpoint = f"{BASE_URL}/booking"
    headers = {"Content-Type": "application/json"}

    # Define the data for creating a booking
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    # Convert the booking data to JSON format
    booking_json = json.dumps(booking_data)

    # Send a POST request to create the booking
    response = requests.post(endpoint, data=booking_json, headers=headers)

    # Assert the response status code (200 indicates success)
    assert response.status_code == 200

    # Verify that the response contains the booking ID
    assert "bookingid" in response.json()


if __name__ == "__main__":
    pytest.main(["-v", "test_create_booking.py"])
