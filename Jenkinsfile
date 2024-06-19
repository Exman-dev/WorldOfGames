pipeline {
    agent any
    environment {
        PATH = "${env.PATH};C:\\Windows\\System32"
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {           
                    bat 'docker build -t davidmihart69969/worldofgames .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    bat 'docker run -d -p 8777:8777 -v %WORKSPACE%\\Scores.txt:/app/Scores.txt --name worldofgames davidmihart69969/worldofgames'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = bat(script: 'docker exec worldofgames python tests/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    bat 'docker stop worldofgames'
                    bat 'docker rm worldofgames'
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                        bat 'docker push davidmihart69969/worldofgames:latest' // Change made here
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
