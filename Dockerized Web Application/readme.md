# Dockerized Web Application

A simple web application configured to run in Docker containers.

## Features

- Containerized web service
- Easy setup with Docker 
- Designed for development and testing

## Getting Started

### Prerequisites

- Docker

### Run the application

1. Build and start the containers:

   ```bash
   docker build -t web-app:1 .
   docker run -it -p 8000:8000 web-app:1
   ```

2. Open the application in your browser at:

   ```
   http://localhost:8000
   ```

### Stop the application

```bash
docker stop < cont id >
```

## Project Structure

- `Dockerfile` - defines the application container image
- `app/ or main.py` - application source code

## Notes

This repository is intended for a Dockerized web application demo and can be extended with additional services, environment configuration, and deployment scripts.
