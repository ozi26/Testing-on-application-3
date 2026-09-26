# Driver Service Tests: checks driver registration and availability.
from sample_microservices.driver_service import app, drivers  # Imports the driver app and state.

def setup_function():  # Runs before every test.
    drivers.clear()  # Clears driver state.

def test_create_driver_unit():  # Tests driver creation.
    client = app.test_client()  # Creates Flask's test client.
    response = client.post("/drivers", json={"id":"d1","name":"Ben","vehicle":"Sedan"})  # Registers a driver.
    assert response.status_code == 201  # Confirms successful creation.
    assert drivers["d1"]["available"] is True  # Confirms the default availability.

def test_available_drivers_integration():  # Tests the availability endpoint.
    client = app.test_client()  # Creates the test client.
    client.post("/drivers", json={"id":"d1","name":"Ben","vehicle":"Sedan"})  # Creates a driver.
    response = client.get("/drivers/available")  # Reads available drivers.
    assert response.status_code == 200  # Confirms successful lookup.
    assert len(response.json["drivers"]) == 1  # Confirms the driver appears.
