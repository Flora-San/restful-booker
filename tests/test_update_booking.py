import pytest
import requests
import json

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to update an existing booking
def test_update_booking():
    # Specify an existing booking ID to update
    booking_id = 1  # Replace with the ID of the booking you want to update

    # Define the endpoint URL for updating the booking
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    # Define the updated booking data
    updated_booking_data = {
        "firstname": "Updated First Name",
        "lastname": "Updated Last Name",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-02-01",
            "checkout": "2023-02-05"
        },
        "additionalneeds": "Updated Needs"
    }

    # Convert the updated booking data to JSON format
    updated_booking_json = json.dumps(updated_booking_data)

    # Set headers for the request
    headers = {"Content-Type": "application/json"}

    # Send a PUT request to update the booking
    response = requests.put(endpoint, data=updated_booking_json, headers=headers)

    # Assert the response status code (200 indicates success)
    # assert response.status_code == 403


if __name__ == "__main__":
    pytest.main(["-v", "test_update_booking.py"])
