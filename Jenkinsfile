pipeline {
    agent any
    def dockerImage

    stages {
        stage('Build') {
            steps {
                docker.withRegistry('https://cloud.canister.io:5000/miquelbar/', 'canister') {
                    dockerImage = docker.build("code:${env.BUILD_ID}")
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
                docker.withRegistry('https://cloud.canister.io:5000/miquelbar/', 'canister') {
                    dockerImage.push()
                }
            }
        }
    }
}