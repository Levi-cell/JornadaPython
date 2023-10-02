FROM ubuntu:latest
LABEL authors="levig"

ENTRYPOINT ["top", "-b"]

# Use an official Python runtime as the base image
FROM python:3.11.5-slim

# Set the working directory in the containe
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "api:app", "--reload", "0.0.0.0", "--port"]


