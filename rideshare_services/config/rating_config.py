# Configuration for the Rating Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Rating Service'  # Stores the display name used by this service.
PORT = int(os.getenv('RATING_PORT', "5006"))  # Reads the service port with a safe default.
DATA_LABEL = 'ratings'  # Stores the name of the service's in-memory data collection.
