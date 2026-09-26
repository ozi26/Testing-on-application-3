# Configuration for the Notification Service; this file keeps service settings in one central config folder.
import os  # Imports the operating-system module for environment variables.

SERVICE_NAME = 'Notification Service'  # Stores the display name used by this service.
PORT = int(os.getenv('NOTIFICATION_PORT', "5007"))  # Reads the service port with a safe default.
DATA_LABEL = 'notifications'  # Stores the name of the service's in-memory data collection.
