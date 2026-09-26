# Rider Service: registers riders and stores their pickup details.
from flask import Flask, jsonify, request  # Imports Flask helpers for HTTP APIs.
from rideshare_services.config.rider_config import SERVICE_NAME, PORT  # Loads service settings from the central config folder.

app = Flask(__name__)  # Creates the Flask application.
riders = {}  # Stores rider records in memory for this prototype.

# Registers a rider and returns the new record.
@app.post("/riders")  # Maps POST /riders to the registration function.
def create_rider():  # Defines the rider registration handler.
    data = request.get_json(silent=True) or {}  # Reads the incoming JSON body.
    rider_id = data.get("id")  # Reads the rider identifier.
    name = data.get("name")  # Reads the rider name.
    pickup = data.get("pickup")  # Reads the pickup location.
    if not rider_id or not name or not pickup:  # Checks that required fields exist.
        return jsonify(error="id, name and pickup are required"), 400  # Returns a validation error.
    if rider_id in riders:  # Checks for duplicate riders.
        return jsonify(error="Rider already exists"), 409  # Rejects a duplicate identifier.
    rider = {"id": rider_id, "name": name, "pickup": pickup}  # Builds the rider record.
    riders[rider_id] = rider  # Stores the rider record.
    return jsonify(rider), 201  # Returns the new rider.

# Returns one rider by identifier.
@app.get("/riders/<rider_id>")  # Maps GET /riders/<id> to the lookup function.
def get_rider(rider_id):  # Defines the rider lookup handler.
    rider = riders.get(rider_id)  # Reads the rider from memory.
    if not rider:  # Checks whether the rider exists.
        return jsonify(error="Rider not found"), 404  # Returns a not-found response.
    return jsonify(rider)  # Returns the rider record.

# Reports service health for deployment checks.
@app.get("/health")  # Maps GET /health to the health handler.
def health():  # Defines the health handler.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns a simple health response.

# Starts the HTTP service when this file is run directly.
if __name__ == "__main__":  # Checks whether Python launched this file directly.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask on all container interfaces.
