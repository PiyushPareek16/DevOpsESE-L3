pipeline {
    agent any

    triggers {
        // Requires GitHub plugin; triggers on push webhook from GitHub
        githubPush()
    }

    environment {
        APP_NAME = 'weather-monitor'
        DOCKER_IMAGE = "${APP_NAME}:${env.GIT_COMMIT ?: 'local'}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                dir('weather-monitor') {
                    sh 'docker version || true'
                    sh 'docker build -t "$DOCKER_IMAGE" .'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'echo "No tests yet - add unit tests here"'
            }
        }

        stage('Image Inspect') {
            steps {
                sh 'docker images | head -n 20'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded after webhook trigger.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}


