# Payment Service Tests: checks payment validation and approval.
from rideshare_services.payment_service import app, payments  # Imports the payment app and state.

def setup_function():  # Runs before each test.
    payments.clear()  # Clears payment state.

def test_payment_approval_unit():  # Tests successful payment.
    client = app.test_client()  # Creates the test client.
    response = client.post("/payments", json={"riderId":"r1","amount":25.5})  # Processes a payment.
    assert response.status_code == 201  # Confirms approval succeeded.
    assert response.json["status"] == "approved"  # Confirms payment status.

def test_payment_rejects_invalid_amount_integration():  # Tests payment validation.
    client = app.test_client()  # Creates the test client.
    response = client.post("/payments", json={"riderId":"r1","amount":0})  # Sends an invalid amount.
    assert response.status_code == 400  # Confirms validation failed.
