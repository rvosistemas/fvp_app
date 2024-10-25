#!/bin/bash
echo "Starting the project with Docker Compose"
docker-compose -f docker-compose.yml -f backend/docker-compose.yml -f frontend/docker-compose.yml up --build
