pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to staging..."
                sh 'python app.py &'
            }
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