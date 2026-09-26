# Matching Service Tests: checks driver selection and no-driver behavior.
from sample_microservices.matching_service import app, active_matches  # Imports the matching app and state.

def setup_function():  # Runs before each test.
    active_matches.clear()  # Clears previous matches.

def test_match_selects_first_driver():  # Tests the basic matching rule.
    client = app.test_client()  # Creates the test client.
    response = client.post("/matches", json={"riderId":"r1","availableDrivers":[{"id":"d1"},{"id":"d2"}]})  # Requests a match.
    assert response.status_code == 201  # Confirms the match was created.
    assert response.json["driverId"] == "d1"  # Confirms the first driver was selected.

def test_match_returns_not_found_without_drivers():  # Tests the no-driver case.
    client = app.test_client()  # Creates the test client.
    response = client.post("/matches", json={"riderId":"r1","availableDrivers":[]})  # Requests a match with no candidates.
    assert response.status_code == 404  # Confirms no match can be created.
