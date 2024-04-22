ARG PYTHON_VERSION=3.11.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "main.py"]


