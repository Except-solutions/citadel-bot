FROM python:3.9.4-slim-buster

# Install system deps:
RUN apt-get update && apt-get install -y build-essential

# Install poetry:
RUN python -m pip install --no-cache-dir "poetry==1.1.8"

# Copying requiremets:
COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

# Add app
COPY . /app
WORKDIR /app
ENV PYTHONPATH /app

# Install requiremets:
RUN poetry export --dev --without-hashes -f requirements.txt --output requirements.txt && \
    pip install --no-cache-dir -r requirements.txt
