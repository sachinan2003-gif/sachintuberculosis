FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy backend code
COPY scripts/ ./scripts/

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel setuptools_scm && \
    pip install --prefer-binary -r requirements.txt && \
    pip install tflite-runtime fastapi uvicorn python-multipart requests opencv-python-headless

# Expose port
EXPOSE 8000

# Run backend
CMD ["python", "scripts/api_server.py"]
