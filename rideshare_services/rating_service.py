# Rating Service: stores rider ratings for completed trips.
from flask import Flask, jsonify, request  # Imports Flask HTTP helpers.
from rideshare_services.config.rating_config import SERVICE_NAME, PORT  # Loads rating configuration.

app = Flask(__name__)  # Creates the Flask application.
ratings = []  # Stores rating records in memory.

# Creates a rating from one to five stars.
@app.post("/ratings")  # Maps POST /ratings to the rating handler.
def create_rating():  # Defines the rating function.
    data = request.get_json(silent=True) or {}  # Reads the JSON body.
    stars = data.get("stars")  # Reads the star value.
    trip_id = data.get("tripId")  # Reads the trip identifier.
    if not isinstance(stars, int) or stars < 1 or stars > 5 or not trip_id:  # Validates rating data.
        return jsonify(error="tripId and integer stars from 1 to 5 are required"), 400  # Returns validation failure.
    rating = {"tripId": trip_id, "stars": stars, "comment": data.get("comment", "")}  # Creates the rating record.
    ratings.append(rating)  # Stores the rating.
    return jsonify(rating), 201  # Returns the new rating.

# Lists ratings for a trip.
@app.get("/ratings/<trip_id>")  # Maps the rating lookup endpoint.
def get_ratings(trip_id):  # Defines the rating lookup function.
    return jsonify(ratings=[r for r in ratings if r["tripId"] == trip_id])  # Returns matching ratings.

# Reports service health.
@app.get("/health")  # Maps GET /health to the health handler.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
