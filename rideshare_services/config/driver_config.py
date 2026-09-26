# Configuration for the Driver Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Driver Service'  # Stores the display name used by this service.
PORT = int(os.getenv('DRIVER_PORT', "5002"))  # Reads the service port with a safe default.
DATA_LABEL = 'drivers'  # Stores the name of the service's in-memory data collection.
