FROM python:3.11

# Create and set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy your Django project into the container
COPY . /app/
