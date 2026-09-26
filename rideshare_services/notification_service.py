# Notification Service: records messages that would be sent to riders or drivers.
from flask import Flask, jsonify, request  # Imports Flask HTTP helpers.
from rideshare_services.config.notification_config import SERVICE_NAME, PORT  # Loads notification configuration.

app = Flask(__name__)  # Creates the Flask application.
notifications = []  # Stores notification records in memory.

# ---------------------------------------------
# Creates a notification record.
# ---------------------------------------------

@app.post("/notifications")  # Maps POST /notifications to the creation function.
def create_notification():  # Defines the notification creation handler.
    data = request.get_json(silent=True) or {}  # Reads the request body.
    recipient = data.get("recipient")  # Reads the recipient.
    message = data.get("message")  # Reads the message.
    if not recipient or not message:  # Validates required fields.
        return jsonify(error="recipient and message are required"), 400  # Returns validation failure.
    notification = {"id": f"note-{len(notifications) + 1}", "recipient": recipient, "message": message, "status": "queued"}  # Builds the notification.
    notifications.append(notification)  # Stores the notification.
    return jsonify(notification), 201  # Returns the queued notification.

# ---------------------------------------------
# Lists all queued notifications.
# ---------------------------------------------
@app.get("/notifications")  # Maps GET /notifications to the list handler.
def list_notifications():  # Defines the notification listing function.
    return jsonify(notifications=notifications)  # Returns all notifications.

# ---------------------------------------------
# Reports service health.
# ---------------------------------------------
@app.get("/health")  # Maps GET /health to the health handler.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
