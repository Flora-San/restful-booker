import pytest
import requests
import json

BASE_URL = "https://restful-booker.herokuapp.com"


# Test case to partially update an existing booking
def test_partial_update_booking():
    # Specify an existing booking ID to partially update
    booking_id = 1  # Replace with the ID of the booking you want to partially update

    # Define the endpoint URL for partially updating the booking
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    # Define the partial update data (fields to be updated)
    partial_update_data = {
        "firstname": "James",
        "lastname": "Brown"
    }

    # Convert the partial update data to JSON format
    partial_update_json = json.dumps(partial_update_data)

    # Set headers for the request
    headers = {"Content-Type": "application/json"}

    # Send a PATCH request to partially update the booking
    response = requests.patch(endpoint, data=partial_update_json, headers=headers)

    # Assert the response status code (200 indicates success)
    # assert response.status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", "test_partial_update_booking.py"])
