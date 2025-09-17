# Use Python slim image
FROM python:3.11-slim

# Set working directory
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

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install numpy first (must be before tensorflow/matplotlib)
RUN pip install "numpy<2"

# Then install all other dependencies from requirements.txt
RUN pip install --prefer-binary -r requirements.txt

# Additional installs for TFLite, FastAPI, OpenCV headless
RUN pip install tflite-runtime fastapi uvicorn python-multipart requests opencv-python-headless

# Expose port
EXPOSE 8000

# Run backend
CMD ["python", "scripts/api_server.py"]
