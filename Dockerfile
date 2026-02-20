# Stage 1: Builder
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

COPY requirements.txt .

# Install to a specific folder
RUN pip install --target=/app/pkgs -r requirements.txt

# Copy application files
COPY . .

# Stage 2: Distroless
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

# Copy everything (app + pkgs) from builder
COPY --from=builder /app /app

# Tell Python to look in our pkgs folder for Flask
ENV PYTHONPATH=/app:/app/pkgs

# Expose the port
EXPOSE 5000

# Run the application
CMD ["main.py"]
