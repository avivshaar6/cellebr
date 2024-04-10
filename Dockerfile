# Use the Python base image
FROM python:3.11.2

# Set app port to environment variable
ARG APP_PORT
ENV APP_PORT=${APP_PORT}

# Set working directory in the container
WORKDIR /server

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the Flask app files into the container
COPY server.py .

# Command to run the Flask application
ENTRYPOINT ["./entrypoint.sh"]