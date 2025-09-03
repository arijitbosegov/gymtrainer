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

## Set up & Run Application locally
- Flask App (foundational version) is created using Python in VS Code Application
- A Template: templates/index.html is also created for the TEMPLATE in VS Code Application
- Now from new terminal run the App on http://127.0.0.1:5000
  
## Initialize Git in Your Project Folder by
  - git init
- Configure Git by
  - git config --global user.name "arijitbose"
  - git config --global user.email "2024ht66023@wilp.bits-pilani.ac.in"
- Add Files and made First Commit
  - git add .
  - git commit -m "Initial commit"
- Created a Remote Repository on GitHub
- Link Local Repo to GitHub Remote
  - git remote add origin https://github.com/arijitbosegov/gymtrainer
  - git remote -v
- Pushing code to GitHub:
  - git push -u origin master
## Pytest
- Install Pytest: pip install pytest pytest-flask
- Organize Test Directory: test_basic.py & conftest.py
- Writing Unit Tests for Flask Routes and Functions
- Run Your Tests: pytest

## Automatically execute all developed Pytest unit tests
- Creating a Script to Run Tests: run_tests.bat then python -m pytest
- Integrate with Continuous Integration (CI) System: Creating .github/workflows/python-tests.yml
- Then Committing and pushing this file

## Building Docker container image
- Verify installation: docker --version
- Creating a Dockerfile in Your Project Root
- Creating requirements.txt
- Build the Docker Image: docker build -t gymtrainer:latest .
- Run the Docker Container Locally: docker run -p 5000:5000 gymtrainer:latest
- Verify the Container: curl http://localhost:5000

## Design and implement a fully automated CI/CD pipeline using GitHub Actions
- Creating GitHub Actions Workflow Directory and File: .github/workflows/
- Inside it, creating a workflow YML file: .github/workflows/ci-cd-pipeline.yml
- Defining the Workflow Configuration in yml file
- Commit and Push the Workflow
  - git add .github/workflows/ci-cd-pipeline.yml
  - git commit -m "Add CI/CD pipeline for Docker build and Pytest"
  - git push origin master

## 👤 Author
-	Name: Arijit Bose
-	BITS ID: 2024ht66023@wilp.bits-pilani.ac.in
-	GitHub ID: arijitbosegov

## 📝 License
For educational and academic purpose

