FROM python:3.9.4-slim-buster

# Install system deps:
RUN apt update && apt install -y build-essential

# Install poetry:
RUN python -m pip install "poetry==1.1.8"

# Copying requiremets:
COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

# Add app
ADD . /app
WORKDIR /app

# Install requiremets:
RUN poetry export -f requirements.txt --output requirements.txt && \
    pip install -r requirements.txt
