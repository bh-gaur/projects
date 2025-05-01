# projects

# GitHub Actions CI/CD Workflow for Project1

This repository contains a GitHub Actions workflow that automates building, pushing, and deploying a Docker image for project1 whenever changes are pushed to the main branch or manually triggered.

    Workflow Overview
    Triggers:
    On a manual trigger (workflow_dispatch).
    On a push to the main branch affecting files under project1/**.
    Environment Variables:
    IMAGE_NAME: Base name for the Docker image (bhgaur/projects).
    Steps Breakdown
    Checkout Repository:
    Pulls the latest code from the GitHub repository.
    Set up Docker Buildx:
    Prepares the environment for advanced Docker builds.
    Log in to Docker Hub:
    Authenticates using GitHub secrets DOCKER_USERNAME and DOCKER_PASSWORD to allow pushing Docker images.
    Build Docker Image:
    Navigates into the project1/ directory.
    Generates a unique image tag based on the Git commit SHA and current timestamp.
    Builds the Docker image and tags it as:
    <DOCKER_USERNAME>/projects:<UNIQUE_TAG>
    Push Docker Image:
    Pushes the built image to Docker Hub under the unique tag.
    Configure SSH for Remote Server:
    Sets up SSH credentials using the private key stored in ACCESS_KEY_SSH secret.
    Adds GitHub to known hosts to prevent SSH warnings.
    SSH into Remote Server:
    Copies the cleanup_docker.sh script from the project1/ directory to the remote server.
    SSHs into the remote server and executes the cleanup_docker.sh script with the newly built image as an argument.
    Secrets and Variables Used
    Secrets:
    DOCKER_USERNAME — Docker Hub username.
    DOCKER_PASSWORD — Docker Hub password.
    ACCESS_KEY_SSH — SSH private key for accessing the remote server.
    Variables:
    SERVER_IP — Public IP address of the remote server.
    cleanup_docker.sh Script
    The cleanup_docker.sh script is responsible for handling the new Docker image on the server, such as:

    Stopping/removing old containers (if any).
    Pulling the new Docker image.
    Running a new container from the updated image.
    (Exact behavior depends on how cleanup_docker.sh is written.)