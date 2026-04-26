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

    post {

        success {
            emailext(
                subject: "✅ SUCCESS: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Build Successful 🎉</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                <p><b>URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                to: "yogesh.shinde@live.in"
            )
        }

        failure {
            emailext(
                subject: "❌ FAILURE: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Build Failed ❌</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Check Console Output:</b></p>
                <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a>
                """,
                to: "yogesh.shinde@live.in"
            )
        }
    }
}