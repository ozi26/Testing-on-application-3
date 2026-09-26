# Rating Service Tests: checks rating creation and lookup.
from sample_microservices.rating_service import app, ratings  # Imports the rating app and state.

def setup_function():  # Runs before each test.
    ratings.clear()  # Clears rating state.

def test_create_rating_unit():  # Tests valid rating creation.
    client = app.test_client()  # Creates the test client.
    response = client.post("/ratings", json={"tripId":"t1","stars":5,"comment":"Good ride"})  # Creates a rating.
    assert response.status_code == 201  # Confirms creation succeeded.
    assert response.json["stars"] == 5  # Confirms the rating value.

def test_get_ratings_integration():  # Tests rating retrieval.
    client = app.test_client()  # Creates the test client.
    client.post("/ratings", json={"tripId":"t1","stars":5})  # Creates test data.
    response = client.get("/ratings/t1")  # Reads ratings for the trip.
    assert response.status_code == 200  # Confirms lookup succeeded.
    assert len(response.json["ratings"]) == 1  # Confirms the rating is returned.
