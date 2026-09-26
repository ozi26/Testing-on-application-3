# Configuration for the Matching Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Matching Service'  # Stores the display name used by this service.
PORT = int(os.getenv('MATCHING_PORT', "5009"))  # Reads the service port with a safe default.(5004)
DATA_LABEL = 'matches'  # Stores the name of the service's in-memory data collection.
