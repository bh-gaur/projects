#!/bin/bash

# Check if the image tag is passed
if [ -z "$1" ]; then
  echo "Error: No image tag provided!"
  exit 1
fi

IMAGE_TAG=$1

# Stop all running containers
echo "Stopping all running containers..."
sudo docker stop $(docker ps -aq)

# Remove all containers (stopped or running)
echo "Removing all containers..."
sudo docker rm $(docker ps -aq)

# Remove all images
echo "Removing all Docker images..."
sudo docker rmi $(docker images -q)

# Pull the new Docker image with the unique tag
echo "Pulling the new Docker image with tag $IMAGE_TAG..."
sudo docker pull $IMAGE_TAG

# Run the new Docker image
echo "Running the new Docker image with tag $IMAGE_TAG..."
sudo docker run -d -p5000:5000 --name app $IMAGE_TAG

# Optional: Clean up unused volumes (if any)
echo "Removing unused Docker volumes..."
sudo docker volume prune -f

# Optional: Clean up unused networks
echo "Removing unused Docker networks..."
sudo docker network prune -f

echo "Docker container with image $IMAGE_TAG is running successfully!"
