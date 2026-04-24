pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        APP_DIR = "/home/ubuntu/flask-app"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/yogeshvshinde/CI-CD-Jenkins-Github.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                ssh ubuntu@localhost << EOF
                cd $APP_DIR || mkdir -p $APP_DIR && cd $APP_DIR
                git pull || git clone https://github.com/yogeshvshinde/CI-CD-Jenkins-Github.git .

                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt

                pkill -f app.py || true
                nohup python app.py > app.log 2>&1 &
                EOF
                '''
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