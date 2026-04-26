pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/yogeshvshinde/CI-CD-Jenkins-Github.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("flask-app-image")
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh 'docker rm -f flask-container || true'
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name flask-container flask-app-image'
                }
            }
        }
    }
}