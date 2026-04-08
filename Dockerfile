# Use lightweight Python base image
FROM python:3.9-slim

# Install debugging tools (curl, wget)
RUN apt-get update && \
    apt-get install -y curl wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose application port (OpenShift standard)
EXPOSE 8080

# Run application using Gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]