# Ride-sharing Microservices Prototype

This project is a deployable prototype of a ride-sharing platform built with **Python, Flask and pytest**. It contains seven services, centralized configuration, unit tests, integration tests, Docker Compose deployment, Jenkins CI configuration, a smoke test, and a small change analyzer for CI experiments.

## Services

| Service | Port | Responsibility |
|---|---:|---|
| Rider | 5001 | Rider registration and pickup details |
| Driver | 5002 | Driver registration and availability |
| Trip | 5003 | Trip lifecycle |
| Matching | 5004 | Driver matching |
| Payment | 5005 | Simulated fare payment |
| Rating | 5006 | Trip ratings |
| Notification | 5007 | Notification queue |

## Prototype note

The prototype keeps state in memory so it can run without a database, cloud platform or Kubernetes. This is intentional for easy demonstration. For production use, replace in-memory state with persistent storage and add authentication, secrets management, durable messaging, observability, rate limiting and stronger transactional behavior.

## Folder structure

```text
Main-Project-2/
├── analyzer/
├── sample_microservices/
│   ├── config/
│   │   ├── rider_config.py
│   │   ├── driver_config.py
│   │   ├── trip_config.py
│   │   ├── matching_config.py
│   │   ├── payment_config.py
│   │   ├── rating_config.py
│   │   └── notification_config.py
│   ├── rider_service.py
│   ├── driver_service.py
│   ├── trip_service.py
│   ├── matching_service.py
│   ├── payment_service.py
│   ├── rating_service.py
│   └── notification_service.py
├── scripts/
├── tests/
├── images/
├── .gitignore
├── analyzer_result.json
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
├── run_selected_tests.py
└── Setup.py
```

## Local setup

1. Install Python 3.11 or newer.
2. Create a virtual environment: `python -m venv .venv`.
3. Activate it.
4. Install dependencies: `pip install -r requirements.txt`.
5. Run tests: `pytest -q`.

## Docker deployment

```bash
docker compose up --build
```

The seven health endpoints are available from ports 5001 through 5007.

Run the smoke test after the containers are ready:

```bash
python scripts/smoke_test.py
```

## Example ride flow

Register a rider:

```bash
curl -X POST http://localhost:5001/riders -H "content-type: application/json" -d '{"id":"r1","name":"Ada","pickup":"Main Street"}'
```

Register a driver:

```bash
curl -X POST http://localhost:5002/drivers -H "content-type: application/json" -d '{"id":"d1","name":"Ben","vehicle":"Sedan"}'
```

Ask the matching service to match the rider to available drivers:

```bash
curl -X POST http://localhost:5004/matches -H "content-type: application/json" -d '{"riderId":"r1","availableDrivers":[{"id":"d1"}]}'
```

Start a trip:

```bash
curl -X POST http://localhost:5003/trips -H "content-type: application/json" -d '{"id":"t1","riderId":"r1","driverId":"d1"}'
```

Pay for the trip:

```bash
curl -X POST http://localhost:5005/payments -H "content-type: application/json" -d '{"riderId":"r1","amount":25.50}'
```

Rate the trip:

```bash
curl -X POST http://localhost:5006/ratings -H "content-type: application/json" -d '{"tripId":"t1","stars":5,"comment":"Good ride"}'
```

Queue a notification:

```bash
curl -X POST http://localhost:5007/notifications -H "content-type: application/json" -d '{"recipient":"r1","message":"Driver is arriving"}'
```

## Testing

Every service has tests covering its main behavior plus HTTP-level integration behavior. The shared health integration test loads all seven service applications and verifies that each exposes a working health endpoint.

## CI/CD

The `Jenkinsfile` creates a virtual environment, installs dependencies, runs pytest, and validates Docker Compose. The Jenkins agent should have Python and Docker installed.

## Configuration

All service configuration is kept under `sample_microservices/config/`, matching the requested layout. Environment variables can override service ports.

## Architecture image

See `images/architecture.svg` for a simple architecture diagram.

## License

This prototype is provided for educational and thesis/project demonstration purposes.
