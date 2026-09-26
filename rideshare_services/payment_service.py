# Payment Service: simulates fare payment authorization.
from flask import Flask, jsonify, request  # Imports Flask HTTP helpers.
from rideshare_services.config.payment_config import SERVICE_NAME, PORT  # Loads payment configuration.

app = Flask(__name__)  # Creates the Flask application.
payments = []  # Stores simulated payments in memory.

# ---------------------------------------------
# Processes a simulated ride payment.
# ---------------------------------------------
@app.post("/payments")  # Maps POST /payments to the payment handler.
def process_payment():  # Defines the payment function.
    data = request.get_json(silent=True) or {}  # Reads the request body.
    amount = data.get("amount")  # Reads the fare amount.
    rider_id = data.get("riderId")  # Reads the rider identifier.
    if not isinstance(amount, (int, float)) or amount <= 0 or not rider_id:  # Validates payment input.
        return jsonify(error="positive numeric amount and riderId are required"), 400  # Returns validation failure.
    payment = {"id": f"pay-{len(payments) + 1}", "riderId": rider_id, "amount": amount, "status": "approved"}  # Creates the payment record.
    payments.append(payment)  # Stores the payment.
    return jsonify(payment), 201  # Returns the payment.

# ---------------------------------------------
# Returns service health.
# ---------------------------------------------

@app.get("/health")  # Maps GET /health to the health handler.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
