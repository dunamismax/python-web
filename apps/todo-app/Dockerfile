# Todo App Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy shared packages
COPY ../../packages /app/packages

# Copy app source
COPY . .

# Initialize Reflex app
RUN reflex init

# Build the app
RUN reflex export

# Expose ports
EXPOSE 3000 8000

# Start the app
CMD ["reflex", "run", "--env", "prod"]