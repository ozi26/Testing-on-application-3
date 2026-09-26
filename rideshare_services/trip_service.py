# Trip Service: starts and completes rides while storing their basic status.
from flask import Flask, jsonify, request  # Imports Flask HTTP helpers.
from rideshare_services.config.trip_config import SERVICE_NAME, PORT  # Loads trip configuration.

app = Flask(__name__)  # Creates the Flask application.
trips = {}  # Stores trip records by identifier.

# Creates a new trip.
@app.post("/trips")  # Maps POST /trips to the trip creation function.
def create_trip():  # Defines the trip creation handler.
    data = request.get_json(silent=True) or {}  # Reads the JSON request body.
    trip_id = data.get("id")  # Reads the trip identifier.
    rider_id = data.get("riderId")  # Reads the rider identifier.
    driver_id = data.get("driverId")  # Reads the driver identifier.
    if not trip_id or not rider_id or not driver_id:  # Validates required trip data.
        return jsonify(error="id, riderId and driverId are required"), 400  # Returns validation failure.
    trip = {"id": trip_id, "riderId": rider_id, "driverId": driver_id, "status": "started"}  # Creates the trip record.
    trips[trip_id] = trip  # Stores the trip.
    return jsonify(trip), 201  # Returns the created trip.

# Completes a trip.
@app.patch("/trips/<trip_id>/complete")  # Maps the completion endpoint.
def complete_trip(trip_id):  # Defines the completion function.
    trip = trips.get(trip_id)  # Reads the trip.
    if not trip:  # Checks whether the trip exists.
        return jsonify(error="Trip not found"), 404  # Returns a not-found response.
    trip["status"] = "completed"  # Changes the trip status.
    return jsonify(trip)  # Returns the completed trip.

# Returns one trip.
@app.get("/trips/<trip_id>")  # Maps the trip lookup endpoint.
def get_trip(trip_id):  # Defines the lookup function.
    trip = trips.get(trip_id)  # Reads the trip record.
    if not trip:  # Checks for an unknown trip.
        return jsonify(error="Trip not found"), 404  # Returns a not-found response.
    return jsonify(trip)  # Returns the trip.

# Reports service health.
@app.get("/health")  # Maps the health endpoint.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
