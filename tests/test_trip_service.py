# Trip Service Tests: checks trip creation and completion.
from rideshare_services.trip_service import app, trips  # Imports the trip app and state.

def setup_function():  # Runs before each test.
    trips.clear()  # Clears trip state.

def test_create_trip_unit():  # Tests trip creation.
    client = app.test_client()  # Creates Flask's test client.
    response = client.post("/trips", json={"id":"t1","riderId":"r1","driverId":"d1"})  # Creates a trip.
    assert response.status_code == 201  # Confirms creation succeeded.
    assert trips["t1"]["status"] == "started"  # Confirms the initial status.

def test_complete_trip_integration():  # Tests trip completion.
    client = app.test_client()  # Creates the test client.
    client.post("/trips", json={"id":"t1","riderId":"r1","driverId":"d1"})  # Creates a test trip.
    response = client.patch("/trips/t1/complete")  # Completes the trip.
    assert response.status_code == 200  # Confirms completion succeeded.
    assert response.json["status"] == "completed"  # Confirms the completed status.
