pipeline {
    agent any

    triggers {
        githubPush()   // Trigger build on GitHub webhook push
    }

    environment {
        IMAGE_NAME = "flask-cicd-app"
        CONTAINER_NAME = "flask-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/yogeshvshinde/CI-CD-Jenkins-Github.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            emailext (
                subject: "SUCCESS: ${env.JOB_NAME}",
                body: "Build succeeded: ${env.BUILD_URL}",
                to: "yogeshvshinde19@gmail.com"
            )
        }

        failure {
            emailext (
                subject: "FAILED: ${env.JOB_NAME}",
                body: "Build failed: ${env.BUILD_URL}",
                to: "yogeshvshinde19@gmail.com"
            )
        }
    }
}