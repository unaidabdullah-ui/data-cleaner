FROM python:3.10-slim

WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Run the app
ENTRYPOINT ["python", "data_cleaner.py"]

