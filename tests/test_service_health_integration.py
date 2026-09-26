# Ride-sharing Integration Tests: checks the health endpoint of every service.
import importlib  # Imports dynamic module loading for the service list.

SERVICE_MODULES = ["rider", "driver", "trip", "matching", "payment", "rating", "notification"]  # Lists all seven services.

def test_all_services_have_health_endpoints():  # Defines the multi-service health integration test.
    for service in SERVICE_MODULES:  # Iterates through every service name.
        module = importlib.import_module(f"rideshare_services.{service}_service")  # Imports the service module.
        client = module.app.test_client()  # Creates a test client for the Flask app.
        response = client.get("/health")  # Calls the service health endpoint.
        assert response.status_code == 200  # Confirms the endpoint responds successfully.
        assert response.json["status"] == "ok"  # Confirms the health response is correct.
