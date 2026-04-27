# Practice Project using Flask

# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
Flask
Flask-PyMongo
python-dotenv
bson
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
MONGO_URI=<your-mongodb-connection-string>
SECRET_KEY=<your-secret-key>
```

### 5. Run the application

```bash
python app.py
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## Project Structure

```
project/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│
├── app.py
├── requirements.txt
└── .env
```

---

## Screenshots

**Home Page**
Lists all students with Edit/Delete buttons.
- <img width="1902" height="607" alt="image" src="https://github.com/user-attachments/assets/a58a6a6d-4978-4769-8074-232e4d31e69d" />


**Add Student**
Form to add a new student.
- <img width="1897" height="801" alt="image" src="https://github.com/user-attachments/assets/d65d25c3-ebb5-410a-adb1-e130ad7c5878" />


**Update Student**
Form pre-filled with student details.
- <img width="1905" height="897" alt="image" src="https://github.com/user-attachments/assets/04febf01-879f-431f-ab07-abcfb993acf1" />



---

## Notes

* Make sure MongoDB is running and accessible via the URI in `.env`
* Delete action includes a confirmation page to prevent accidental deletion
* Uses `ObjectId` from `bson` to work with MongoDB document IDs
* If you use MongoDB Atlas on macOS, install dependencies again (`pip install -r requirements.txt`). This project now uses `certifi` CA bundle explicitly to avoid common TLS certificate verification failures with `pymongo`.

---

## License

MIT License

---


# Flask CI/CD Pipeline with Jenkins, Docker and MongoDB

## Project Overview

This project demonstrates a complete CI/CD pipeline using:

* Jenkins for automation
* Docker for containerization
* Flask as the web application
* MongoDB as the database
* Azure Ubuntu VM as the hosting environment

The application is deployed on a single Ubuntu VM that serves as:

* Jenkins server
* Application server
* Database host (via Docker container)

---

## Architecture

GitHub Repo -> Jenkins Pipeline -> Docker Build -> Docker Run -> Flask App
-> MongoDB Container

---

## Tech Stack

* Python (Flask)
* Docker
* Jenkins
* MongoDB (Docker container)
* Azure Virtual Machine (Ubuntu)

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── templates/
│   ├── index.html
│   ├── add_student.html
│   └── update_student.html
```

---

## Setup Instructions

### 1. Prerequisites

* Ubuntu VM (Azure)
* Jenkins installed
* Docker installed
* Git installed

---

### 2. Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

---

### 3. Create Docker Network

```bash
docker network create mynet
```

---

### 4. Run MongoDB Container

```bash
docker run -d \
--name mongodb \
--network mynet \
-p 27017:27017 \
mongo
```

---

### 5. Build Flask Docker Image

```bash
docker build -t flask-app-image .
```

---

### 6. Run Flask Container

```bash
docker run -d \
--name flask-container \
--network mynet \
-p 5000:5000 \
-e MONGO_URI="mongodb://mongodb:27017/mydb" \
flask-app-image
```

---

## Jenkins CI/CD Pipeline

### Pipeline Stages

1. Clone GitHub repository
2. Build Docker image
3. Stop existing container
4. Deploy new container

---

### Sample Jenkinsfile

```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Saima-Devops/Flask-App-CI-CD-Pipeline.git'
            }
        }

        stage('Build Image') {
            steps {
                script {
                    docker.build("flask-app-image")
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f flask-container || true'
                sh '''
                docker run -d \
                --name flask-container \
                --network mynet \
                -p 5000:5000 \
                -e MONGO_URI="mongodb://mongodb:27017/mydb" \
                flask-app-image
                '''
            }
        }
    }
}
```

---

## Application Access

Flask App:
http://<VM-PUBLIC-IP>:5000

Health Check:
http://<VM-PUBLIC-IP>:5000/health

---

## Features

* Add, update, delete student records
* MongoDB integration
* Dockerized deployment
* CI/CD pipeline using Jenkins
* Environment variable configuration

---

## Evidence for Assessment

Included screenshots of:

* Jenkins pipeline success
* Docker containers running (docker ps)
* Flask app UI (home page)
* Add, update, delete operations
* MongoDB data (mongosh)
* Email notifications (if configured)

---

## Key Learnings

* CI/CD pipeline implementation using Jenkins
* Containerization using Docker
* Service communication using Docker networks
* Environment-based configuration
* Debugging containerized applications


---

## Conclusion

This project demonstrates a complete end-to-end DevOps pipeline integrating source control, automation, containerization and deployment on a cloud VM.

## GitHub Actions CI/CD Pipeline

This project uses GitHub Actions to automate CI/CD.

### Workflow Overview

- On push to staging:
  - Install dependencies
  - Run tests
  - Build Docker image
  - Deploy to staging server

- On release:
  - Deploy to production server

### Required Secrets

Configure the following secrets in GitHub:

- STAGING_HOST
- STAGING_USER
- PROD_HOST
- PROD_USER


### Deployment

The application is deployed using SSH into the Azure VM and running Docker containers.

