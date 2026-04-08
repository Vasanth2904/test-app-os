# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# OpenShift best practice: run on non-root port
EXPOSE 8080

# Run using gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]