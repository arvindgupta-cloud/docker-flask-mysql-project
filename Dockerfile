# Use official Python image
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

COPY --from=builder /app /app
# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
