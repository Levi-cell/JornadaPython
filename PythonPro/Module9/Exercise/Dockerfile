## Use an official Python runtime as the base image
FROM python:3.11.5-slim

# Create the application's working directory
WORKDIR /app
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on
EXPOSE 8000

# Command to start the server
CMD ["python", "./rick_morty_project/manage.py" ,"runserver", "0.0.0.0:8000"]