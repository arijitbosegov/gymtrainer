# GymTrainer Flask Application

This is the Flask-based GymTrainer web application.

## Features

- Core Flask app for gym management
- Dockerized for consistent environment
- Automated testing using Pytest
- CI/CD pipeline setup with GitHub Actions

## Setup Instructions

1. Clone the repo:
git clone https://github.com/arijitbosegov/gymtrainer.git
2. Build Docker image:
docker build -t gymtrainer:latest .
3. Run Docker container:
docker run -p 5000:5000 gymtrainer:latest
4. Run tests manually (optional):
pytest

## CI/CD Pipeline

- Automated Docker build and test on every push via GitHub Actions.
- CI/CD workflow file located at `.github/workflows/ci-cd-pipeline.yml`.

