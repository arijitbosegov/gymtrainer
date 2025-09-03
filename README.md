# 🏃‍♂️GymTrainer Flask Application

This project is a web-based fitness tracker designed for managing personal workouts. It was developed for a DevOps assignment to showcase best practices in version control, unit testing, Docker containerization, and CI/CD automation with GitHub Actions.

## 📊 Structure

gymtrainer/ ├── gymtrainer.py # Main Flask application ├── test_basic.py & coftest.py # Pytest unit tests ├── requirements.txt # Python dependencies ├── Dockerfile # Docker configuration ├── .github/ │ └── workflows/ │ └── pythontests.yml & ci-cd-pipeline.yml # GitHub Actions CI/CD pipeline └── README.md # Project documentation

## ✨ Features

- Core Flask app for gym management
- Dockerized for consistent environment
- Automated testing using Pytest
- CI/CD pipeline setup with GitHub Actions

## 🤖 Technologies
- Python 3.9+
- Flask
- Pytest
- Docker
- Git & GitHub
- GitHub Actions

## 🛠️ Setup Instructions

1. Clone the repo:
git clone https://github.com/arijitbosegov/gymtrainer.git
2. Build Docker image:
docker build -t gymtrainer:latest .
3. Run Docker container:
docker run -p 5000:5000 gymtrainer:latest
4. Run tests manually (optional):
pytest

## 📊 CI/CD Pipeline

- Automated Docker build and test on every push via GitHub Actions.
- CI/CD workflow file located at `.github/workflows/ci-cd-pipeline.yml`.

## 👤 Author
-	Name: Arijit Bose
-	BITS ID: 2024ht66023@wilp.bits-pilani.ac.in
-	GitHub ID:

## 📝 License
For educational and academic purpose

