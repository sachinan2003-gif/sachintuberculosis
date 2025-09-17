# Use Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy backend code
COPY scripts/ ./scripts/

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --prefer-binary -r requirements.txt

# Expose port
EXPOSE 8000

# Run backend
CMD ["python", "scripts/api_server.py"]
