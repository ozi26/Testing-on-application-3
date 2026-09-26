# Matching Service: finds the first available driver for a rider request.
from flask import Flask, jsonify, request  # Imports Flask HTTP helpers.
from sample_microservices.config.matching_config import SERVICE_NAME, PORT  # Loads matching configuration.

app = Flask(__name__)  # Creates the Flask application.
active_matches = {}  # Stores current rider-to-driver matches.

# Creates a ride match using a supplied driver list.
@app.post("/matches")  # Maps POST /matches to the matching function.
def create_match():  # Defines the matching handler.
    data = request.get_json(silent=True) or {}  # Reads the request body.
    rider_id = data.get("riderId")  # Reads the rider identifier.
    drivers = data.get("availableDrivers") or []  # Reads candidate drivers.
    if not rider_id or not isinstance(drivers, list):  # Validates the request.
        return jsonify(error="riderId and availableDrivers are required"), 400  # Returns validation failure.
    if not drivers:  # Checks whether there are candidates.
        return jsonify(error="No driver available"), 404  # Reports that no driver can be matched.
    match = {"riderId": rider_id, "driverId": drivers[0].get("id"), "status": "matched"}  # Chooses the first available driver.
    active_matches[rider_id] = match  # Stores the match.
    return jsonify(match), 201  # Returns the match.

# Returns a rider's current match.
@app.get("/matches/<rider_id>")  # Maps the match lookup endpoint.
def get_match(rider_id):  # Defines the match lookup handler.
    match = active_matches.get(rider_id)  # Reads the match.
    if not match:  # Checks for an unknown rider.
        return jsonify(error="Match not found"), 404  # Returns a not-found response.
    return jsonify(match)  # Returns the match.

# Reports service health.
@app.get("/health")  # Maps the health endpoint.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
