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

                    dockerImage = docker.build("davidmihart69969/worldofgames")
                }
            }
        }
        stage('Run') {
            steps {
                script {

                    app = dockerImage.run('-p 8777:8777 -v $WORKSPACE/Scores.txt:/app/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {

                    def result = app.inside {
                        sh 'python tests/e2e.py'
                    }
                    if (result != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {

                    app.stop()

                    docker.withRegistry('', DOCKER_CREDENTIALS_ID) {
                        dockerImage.push("latest")
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

