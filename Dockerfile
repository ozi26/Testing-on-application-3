# Uses a small official Python runtime image.
FROM python:3.13-slim
# Sets the application working directory.
WORKDIR /app
# Copies dependency requirements into the image.
COPY requirements.txt ./
# Installs Python dependencies without retaining pip's cache.
RUN pip install --no-cache-dir -r requirements.txt
# Copies the microservice source and central configuration.
COPY sample_microservices ./sample_microservices
# Adds the service directory to Python's import path.
ENV PYTHONPATH=/app
# Defines the service module selected by Docker Compose.
ARG SERVICE_FILE
# Stores the service file name as an environment variable.
ENV SERVICE_FILE=${SERVICE_FILE}
# Starts the selected Flask service.
CMD ["sh", "-c", "python sample_microservices/${SERVICE_FILE}"]
