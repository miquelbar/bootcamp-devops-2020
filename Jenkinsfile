def dockerImage
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("miquelbar/code:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            when {
                expression { env.BRANCH_NAME != 'master' }
            }
            steps {
                script {
                    sh "make test"
                }
            }
        }
        stage('Deploy') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                echo 'Deploying....'
                script {
                    docker.withRegistry('https://cloud.canister.io:5000', 'canister') {
                        dockerImage.push()
                    }
                    sh "sed -i'' 's/{{BUILD_ID}}/${env.BUILD_ID}/g' kubernetes/deployment.yml"
                    sh "cat kubernetes/deployment.yml"
                    sh "kubectl apply -f kubernetes/"
                }
            }
        }
    }
}