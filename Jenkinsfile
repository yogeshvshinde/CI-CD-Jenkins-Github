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

    post {
        success {
            echo "Build succeeded"
        }
        failure {
            echo "Build failed"
        }
    }
}