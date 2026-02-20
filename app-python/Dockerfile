# Use the official Python image based on Alpine Linux
FROM python:alpine

# Set the working directory inside the container to /app
WORKDIR /app

# Uncomment to copy requirements file for dependencies
#COPY requirements.txt .

# Uncomment to install dependencies from requirements.txt
#RUN pip install -r requirements.txt

# Copy the Python script into the working directory
COPY app/script.py .

# Run the Python script when the container starts
CMD ["python", "script.py"]
