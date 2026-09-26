# Configuration for the Rider Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Rider Service'  # Stores the display name used by this service.
PORT = int(os.getenv('RIDER_PORT', "5001"))  # Reads the service port with a safe default.
DATA_LABEL = 'riders'  # Stores the name of the service's in-memory data collection.
