# Configuration for the Trip Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Trip Service'  # Stores the display name used by this service.
PORT = int(os.getenv('TRIP_PORT', "5003"))  # Reads the service port with a safe default.
DATA_LABEL = 'trips'  # Stores the name of the service's in-memory data collection.
