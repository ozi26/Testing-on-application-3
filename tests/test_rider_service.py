# Rider Service Tests: checks registration and lookup.
from sample_microservices.rider_service import app, riders  # Imports the rider service app and state.

def setup_function():  # Runs before each test function.
    riders.clear()  # Resets rider state.

def test_create_rider_unit():  # Tests the rider state after registration through HTTP.
    client = app.test_client()  # Creates Flask's test client.
    response = client.post("/riders", json={"id":"r1","name":"Ada","pickup":"Main Street"})  # Registers a rider.
    assert response.status_code == 201  # Confirms successful creation.
    assert riders["r1"]["name"] == "Ada"  # Confirms the state contains the rider.

def test_get_rider_integration():  # Tests rider lookup through the HTTP route.
    client = app.test_client()  # Creates the test client.
    client.post("/riders", json={"id":"r1","name":"Ada","pickup":"Main Street"})  # Creates test data.
    response = client.get("/riders/r1")  # Requests the rider.
    assert response.status_code == 200  # Confirms successful lookup.
    assert response.json["pickup"] == "Main Street"  # Confirms the returned data.
