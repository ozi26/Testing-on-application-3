# Driver Service: registers drivers and tracks their availability.
from flask import Flask, jsonify, request  # Imports Flask helpers for HTTP APIs.
from rideshare_services.config.driver_config import SERVICE_NAME, PORT  # Loads driver configuration.

app = Flask(__name__)  # Creates the Flask application.
drivers = {}  # Stores driver records in memory.

# Registers a driver.
@app.post("/drivers")  # Maps POST /drivers to the creation handler.
def create_driver():  # Defines the driver creation function.
    data = request.get_json(silent=True) or {}  # Reads the JSON body.
    driver_id = data.get("id")  # Reads the driver identifier.
    name = data.get("name")  # Reads the driver name.
    vehicle = data.get("vehicle")  # Reads the vehicle description.
    if not driver_id or not name or not vehicle:  # Validates required fields.
        return jsonify(error="id, name and vehicle are required"), 400  # Returns a validation error.
    if driver_id in drivers:  # Checks for duplicate drivers.
        return jsonify(error="Driver already exists"), 409  # Rejects duplicates.
    driver = {"id": driver_id, "name": name, "vehicle": vehicle, "available": True}  # Builds a driver record.
    drivers[driver_id] = driver  # Stores the driver.
    return jsonify(driver), 201  # Returns the new driver.

# ---------------------------------------------
# Lists drivers that are currently available.
# -------------------------------------------
@app.get("/drivers/available")  # Maps the available-driver endpoint.
def available_drivers():  # Defines the available-driver handler.
    return jsonify(drivers=[d for d in drivers.values() if d["available"]])  # Returns only available drivers.

# Marks one driver as available or unavailable.
@app.patch("/drivers/<driver_id>/availability")  # Maps the availability update endpoint.
def update_availability(driver_id):  # Defines the availability update function.
    driver = drivers.get(driver_id)  # Reads the driver record.
    if not driver:  # Checks for an unknown driver.
        return jsonify(error="Driver not found"), 404  # Returns a not-found response.
    driver["available"] = bool((request.get_json(silent=True) or {}).get("available", True))  # Updates availability.
    return jsonify(driver)  # Returns the updated driver.

# Reports service health.
@app.get("/health")  # Maps the health endpoint.
def health():  # Defines the health function.
    return jsonify(status="ok", service=SERVICE_NAME)  # Returns service health.

# Starts the service when run directly.
if __name__ == "__main__":  # Checks for direct execution.
    app.run(host="0.0.0.0", port=PORT)  # Starts Flask.
