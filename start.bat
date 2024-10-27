@echo off
docker-compose -f docker-compose.yml -f backend/docker-compose.yml -f frontend/docker-compose.yml up --build
pause
