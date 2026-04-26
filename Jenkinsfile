pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Saima-Devops/Flask-App-CI-CD-Pipeline.git'
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