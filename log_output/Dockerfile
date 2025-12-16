# Use a lightweight Python base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY main.py .

# Run the python application with unbuffered output
CMD ["python", "-u", "main.py"]
