pipeline {
    agent any

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
                    app = dockerImage.run('-p 8777:8777 -v $PWD/Scores.txt:/app/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: "python tests/e2e.py", returnStatus: true)
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
                    docker.withRegistry('', 'dockerhub-credentials') {
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
