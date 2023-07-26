# Use an official lightweight Python image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory in container to /app
WORKDIR /app 
# Copy the current directory contents into the container at /app
COPY requirements.txt /app/
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0