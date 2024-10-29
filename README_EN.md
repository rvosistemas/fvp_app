FVP_APP
This is a financial platform project that uses a FastAPI backend and an Angular frontend. This README will guide you to set up the development environment, run tests, and deploy the project in production using Docker.

Prerequisites
Docker and Docker Compose
Node.js and npm (for Angular development outside of Docker)
Python 3.9+ and pip (for FastAPI development outside of Docker)
Project Structure
backend/: Contains the FastAPI code and configuration.
frontend/: Contains the Angular code.
docker-compose.yml: Docker Compose configuration for development.
docker-compose.prod.yml: Docker Compose configuration for production.
Setting Up the Development Environment
Clone the repository:

bash

git clone https://github.com/your_user/fvp_app.git
cd fvp_app
Create an .env file in the backend folder based on the .env.example file, setting up the necessary variables to connect to the local database.

1. Start the Development Environment with Docker
To run the project in Docker in development mode:

bash

docker-compose up --build
This command will start the containers for nginx, fastapi-backend, and angular-frontend.

2. Start the Development Environment Locally (Without Docker)
Backend - FastAPI
Navigate to the backend folder and create a virtual environment:

bash

cd backend
python3 -m venv env
source env/bin/activate
Install the dependencies:

bash

pip install -r requirements.txt
Set up the database and apply migrations with Alembic:

bash

alembic upgrade head
Run the development server:

bash

uvicorn app.main:app --reload
The backend will be available at http://localhost:8000.

Frontend - Angular
Navigate to the frontend folder and install dependencies:

bash

cd frontend
npm install
Run the development server:

bash

ng serve
The frontend will be available at http://localhost:4200.

Running Tests
Backend Tests (FastAPI)
Navigate to the backend folder.

Ensure you are in the virtual environment (if running locally).

Run tests with pytest:

bash

pytest
To generate a coverage report:

bash

pytest --cov=app
Frontend Tests (Angular)
Navigate to the frontend folder.

Run unit tests with Karma:

bash

ng test
To generate a coverage report:

bash

ng test --code-coverage
Coverage reports will be located in the coverage folder within the frontend project.

Setting Up the Production Environment
To run the project in production mode using Docker:

Ensure the .env.production file is configured in the backend folder.

Run the following command to start the project in production:

bash

docker-compose -f docker-compose.prod.yml up --build -d
This command will start the containers in "detached" mode (-d) to run in the background.

Important Notes
Nginx: Nginx acts as a reverse proxy to direct traffic to the frontend and backend. The configuration is in nginx.conf.
Production Database: In the .env.production file, configure POSTGRES_DATABASE_URL with the URL of the AWS RDS or the database service you are using in production.
CORS Permissions: In the backend’s main.py file, we have allowed CORS so that the frontend can communicate with the backend.
Project Structure
plaintext

.
├── backend
│   ├── alembic             # Migration manager
│   ├── app                 # FastAPI application code
│   ├── Dockerfile          # Dockerfile for FastAPI
│   └── requirements.txt    # FastAPI dependencies
├── frontend
│   ├── src                 # Angular application code
│   ├── Dockerfile          # Dockerfile for Angular
│   └── angular.json        # Angular project configuration
├── docker-compose.yml      # Configuration for development
└── docker-compose.prod.yml # Configuration for production
Troubleshooting
Connection Error between Frontend and Backend: Ensure that CORS is configured correctly and that URLs are set correctly in ApiService in the frontend.
Issues with Alembic Migrations: Check the alembic.ini file and ensure that the database connection string is correct.
Docker Permission Errors: Ensure that containers have the correct permissions to access necessary volumes or files.
You now have a complete guide to running and testing your project in both development and production environments.

vbnet


This README provides a complete guide in English on how to set up the development environment, run tests, and configure production deployment. Adjust any specific URLs or paths as necessary for your project.





