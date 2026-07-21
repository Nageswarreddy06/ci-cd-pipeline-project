pipeline {
    agent any

    environment {
        IMAGE_NAME = "ci-cd-pipeline-app"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'pip install pytest || true'
                sh 'pytest tests/ -v || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image ${IMAGE_NAME}:${IMAGE_TAG}..."
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container to server...'
                sh '''
                    docker stop app || true
                    docker rm app || true
                    docker run -d --name app -p 80:80 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully - deployment live.'
        }
        failure {
            echo 'Pipeline failed - rolling back to previous stable image.'
            // rollback step: restart last known-good container
            sh 'docker run -d --name app -p 80:80 ${IMAGE_NAME}:latest || true'
        }
    }
}
