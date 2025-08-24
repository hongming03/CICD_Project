# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
# Using --no-cache-dir to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Expose the port
# Techincally not needed, it only serves as documentation
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]

# docker run -p <host_port>:<container_port(in this case, Flask Port)> <image_name>
# Access the app via 0.0.0.0:<host_port>
