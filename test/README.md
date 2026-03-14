# Python Test Application

A simple Flask application for testing Jenkins CI/CD pipeline.

## Features

- **Health Check**: `/health` endpoint for Kubernetes readiness probes
- **Home**: `/` endpoint with basic app information
- **Info**: `/api/info` endpoint with environment details
- **Echo**: `/api/echo` POST endpoint for testing

## Local Development

### Prerequisites
- Python 3.8+
- Docker (optional)

### Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   python app.py
   ```

3. **Test endpoints**:
   ```bash
   # Health check
   curl http://localhost:5000/health
   
   # Home endpoint
   curl http://localhost:5000/
   
   # Info endpoint
   curl http://localhost:5000/api/info
   
   # Echo endpoint
   curl -X POST -H "Content-Type: application/json" \
        -d '{"message": "Hello"}' \
        http://localhost:5000/api/echo
   ```

### Docker

1. **Build image**:
   ```bash
   docker build -t python-test-app .
   ```

2. **Run container**:
   ```bash
   docker run -p 5000:5000 python-test-app
   ```

## Jenkins Pipeline

The `Jenkinsfile` includes:

1. **Code Checkout**: Pulls from GitHub
2. **Code Quality**: Flake8 and Pylint checks
3. **Testing**: Pytest with JUnit reports
4. **Docker Build**: Creates container image
5. **Container Testing**: Validates running container
6. **Image Push**: Deploys to DockerHub

### Pipeline Triggers
- Polls GitHub every 5 minutes
- Runs on any changes to the repository

### Environment Variables
- `DOCKER_REPO`: DockerHub repository name
- `IMAGE_TAG`: Unique build identifier
- `DOCKER_CRED`: Jenkins credential ID for DockerHub

## Health Checks

The application includes built-in health checks:

- **Kubernetes Ready**: `/health` endpoint
- **Docker Health**: Built-in container health check
- **Liveness**: Application responds to HTTP requests

## Security Considerations

- Runs as non-root user in container
- Minimal Python base image
- Health checks for monitoring
- No sensitive data in logs
