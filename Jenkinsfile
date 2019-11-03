def dockerImage
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.withRegistry('https://cloud.canister.io:5000', 'canister') {
                        dockerImage = docker.build("miquelbar/code:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                script {
                    docker.withRegistry('https://cloud.canister.io:5000', 'canister') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}