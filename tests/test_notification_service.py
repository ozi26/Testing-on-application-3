# Notification Service Tests: checks notification queuing and listing.
from sample_microservices.notification_service import app, notifications  # Imports the notification app and state.

def setup_function():  # Runs before every test.
    notifications.clear()  # Clears notification state.

def test_create_notification_unit():  # Tests notification creation.
    client = app.test_client()  # Creates the test client.
    response = client.post("/notifications", json={"recipient":"r1","message":"Driver found"})  # Queues a notification.
    assert response.status_code == 201  # Confirms queuing succeeded.
    assert notifications[0]["status"] == "queued"  # Confirms notification state.

def test_list_notifications_integration():  # Tests notification listing.
    client = app.test_client()  # Creates the test client.
    client.post("/notifications", json={"recipient":"r1","message":"Driver found"})  # Creates a notification.
    response = client.get("/notifications")  # Lists notifications.
    assert response.status_code == 200  # Confirms the endpoint succeeded.
    assert len(response.json["notifications"]) == 1  # Confirms the notification is returned.
