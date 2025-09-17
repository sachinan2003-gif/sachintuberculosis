# Use Python slim image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy backend code (scripts folder)
COPY scripts/ ./scripts/

# Copy the trained model file into container root
COPY scripts/tb_model.h5 ./scripts/tb_model.h5

# Copy requirements.txt into container
COPY requirements.txt .

# Upgrade pip and essential build tools
RUN pip install --upgrade pip setuptools wheel setuptools_scm

# Install dependencies
RUN pip install --prefer-binary -r requirements.txt

# Expose the port
EXPOSE 8000

# Run your backend server
CMD ["python", "scripts/api_server.py"]
